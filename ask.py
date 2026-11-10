"""Ask the English Class 9 Book Assistant a question or browse by page.

    python ask.py                                      # chat interactively
    python ask.py -q "Page 33"                         # pick questions from Page 33
    python ask.py -q "Who was Sachin's coach?"
    python ask.py --model qwen2.5:0.5b
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

from prompt import SYSTEM, make_message

DATA_FILE = Path(__file__).parent / "cleaned_english_class9.json"
QA_FILE = Path(__file__).parent / "textbook_qa.json"
PAGE_INDEX_FILE = Path(__file__).parent / "mobile_app" / "assets" / "page_index.json"

if not DATA_FILE.exists():
    raise FileNotFoundError(f"Cleaned book data not found: {DATA_FILE}")

BOOK_PAGES = json.loads(DATA_FILE.read_text(encoding="utf-8"))
QA_BANK = json.loads(QA_FILE.read_text(encoding="utf-8")) if QA_FILE.exists() else []
PAGE_INDEX = json.loads(PAGE_INDEX_FILE.read_text(encoding="utf-8")) if PAGE_INDEX_FILE.exists() else {}

STOP = set(
    "a an the is are was were of for to in on at and or do does did i my me you your what whats how "
    "can could when who whom which where there it be been with about tell please much many have has had will would if any get "
    "this that these those from by".split()
)


def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP


def check_page_or_unit(query):
    q = query.lower().strip()
    page_match = re.search(r'(?:book\s+)?(?:page|p\.?)\s*([0-9]{1,3})', q)
    if not page_match and re.match(r'^[0-9]{1,3}$', q):
        page_match = re.match(r'^([0-9]{1,3})$', q)

    if page_match:
        page_no = page_match.group(1)
        if page_no in PAGE_INDEX.get("pages", {}):
            return {
                "type": "page",
                "page": page_no,
                "data": PAGE_INDEX["pages"][page_no]
            }

    unit_match = re.search(r'unit\s*([0-9]+)', q)
    if unit_match:
        unit_id = int(unit_match.group(1))
        unit_info = next((u for u in PAGE_INDEX.get("units", []) if u["id"] == unit_id), None)
        if unit_info:
            unit_questions = []
            for p in unit_info.get("pages", []):
                p_str = str(p)
                for q_item in PAGE_INDEX.get("pages", {}).get(p_str, {}).get("questions", []):
                    if q_item not in unit_questions:
                        unit_questions.append(q_item)
            return {
                "type": "unit",
                "unit": unit_info["title"],
                "questions": unit_questions
            }
    return None


def find_qa_direct(question):
    q_norm = re.sub(r'[^a-z0-9 ]', '', question.lower()).strip()
    q_w = words(question)

    for item in QA_BANK:
        for alias in item.get("aliases", []):
            if q_norm == alias:
                return item
        if q_norm == re.sub(r'[^a-z0-9 ]', '', item["question"].lower()).strip():
            return item

    best_item, best_score = None, 0
    for item in QA_BANK:
        target_words = words(item["question"])
        overlap = len(q_w & target_words)
        if len(q_w) > 0 and (overlap / len(q_w)) >= 0.70 and overlap > best_score:
            best_score = overlap
            best_item = item
    return best_item


def find_excerpt(question):
    q = words(question)
    best_chunk, best_score, best_page = None, 0, None
    for p in BOOK_PAGES:
        text = p["text"]
        if "a) " in text and "b) " in text and "c) " in text:
            continue
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for i in range(len(sentences)):
            chunk = " ".join(sentences[i:i+4])
            c_words = words(chunk)
            score = len(q & c_words)
            if score > best_score:
                best_chunk, best_score, best_page = chunk, score, p
    return best_chunk, best_page


def ask_ollama(question, excerpt, page_no, model="qwen2.5:0.5b", host="http://localhost:11434"):
    body = json.dumps({
        "model": model,
        "stream": False,
        "options": {"temperature": 0.0},
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": make_message(question, excerpt, page_no)},
        ],
    }).encode("utf-8")
    req = urllib.request.Request(f"{host}/api/chat", data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode("utf-8"))["message"]["content"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Model '{model}' not found in Ollama. Run 'ollama list'."
        return f"Ollama error: {e}"
    except urllib.error.URLError:
        return "Could not reach Ollama. Start Ollama, then try again."


def run(question, model):
    picker = check_page_or_unit(question)
    if picker:
        if picker["type"] == "page":
            d = picker["data"]
            print(f"\n📘 BOOK PAGE {picker['page']} • {d.get('unit')} ({d.get('title')})")
            print("Pick a question number to get the answer:")
            for idx, q_text in enumerate(d.get("questions", []), 1):
                print(f"  [{idx}] {q_text}")
        else:
            print(f"\n📚 {picker['unit']}")
            for idx, q_text in enumerate(picker.get("questions", []), 1):
                print(f"  [{idx}] {q_text}")
        return

    qa_hit = find_qa_direct(question)
    if qa_hit:
        print(f"\n1) DIRECT HIT: [Book Page {qa_hit['page']}] Matching Question: '{qa_hit['question']}'")
        print(f"2) CITATION  : \"{qa_hit['evidence']}\"")
        print(f"3) ANSWER    :\n{qa_hit['answer']}")
        return

    excerpt, page = find_excerpt(question)
    page_no = page["book_page"] if page else None
    print(f"\n1) FIND   : [Book Page {page_no if page_no else '?'}] {excerpt[:120] if excerpt else 'No match'}...")
    print("2) BUILD  : message sent to model:")
    print("   " + make_message(question, excerpt, page_no).replace("\n", "\n   "))
    print("3) ASK    :", ask_ollama(question, excerpt, page_no, model))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="English Class 9 Textbook Assistant")
    ap.add_argument("-q", "--question")
    ap.add_argument("--model", default="qwen2.5:0.5b")
    args = ap.parse_args()
    if args.question:
        run(args.question, args.model)
        return
    print("English Class 9 Textbook Assistant (type 'exit' to quit)")
    while True:
        try:
            q = input("\nStudent> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("exit", "quit", "q"):
            break
        if q:
            run(q, args.model)


if __name__ == "__main__":
    main()
