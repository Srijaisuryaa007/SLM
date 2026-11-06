"""Ask the English Class 9 Book Assistant a question.

    python ask.py                                      # chat interactively
    python ask.py -q "Who were Sachin's favourite players?"
    python ask.py --model qwen2.5:0.5b

What happens for every question:
    1. FIND   the matching excerpt from English class 9.pdf (cleaned_english_class9.json)
    2. BUILD  the prompt with the excerpt and zero-hallucination rules
    3. ASK    the local SLM via Ollama
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
if not DATA_FILE.exists():
    raise FileNotFoundError(f"Cleaned book data not found: {DATA_FILE}")

BOOK_PAGES = json.loads(DATA_FILE.read_text(encoding="utf-8"))

# Small filler words that say nothing about the topic
STOP = set(
    "a an the is are was were of for to in on at and or do does did i my me you your what whats how "
    "can could when who whom which where there it be been with about tell please much many have has had will would if any get "
    "this that these those from by".split()
)


def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP


def find_excerpt(question):
    """Find the most relevant 4-sentence excerpt from the English Class 9 textbook."""
    q = words(question)
    best_chunk, best_score, best_page = None, 0, None
    for p in BOOK_PAGES:
        sentences = re.split(r'(?<=[.!?])\s+', p["text"])
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
