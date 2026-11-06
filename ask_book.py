"""Grounded Q&A on Tamil Nadu Class 9 English Textbook.

Usage:
    python ask_book.py -q "Who were Sachin's favourite players?"
    python ask_book.py -q "What did Sachin do during the thirty minute break?"
    python ask_book.py                                # Interactive chat mode
"""
import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

DATA_FILE = Path(__file__).parent / "cleaned_english_class9.json"

if not DATA_FILE.exists():
    print(f"Error: {DATA_FILE} not found. Run clean_book.py first.")
    sys.exit(1)

BOOK_PAGES = json.loads(DATA_FILE.read_text(encoding="utf-8"))

STOP = set(
    "a an the is are was were of for to in on at and or do does did i my me you your what whats how "
    "can could when who whom which where there it be been with about tell please much many have has had will would if any get "
    "this that these those from by".split()
)

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP

def find_best_context(question):
    q_words = tokenize(question)
    best_chunk, best_score, best_page = None, 0, None

    for p in BOOK_PAGES:
        # Split page text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', p["text"])
        # Group into sliding 4-sentence windows
        for i in range(len(sentences)):
            chunk = " ".join(sentences[i:i+4])
            c_words = tokenize(chunk)
            score = len(q_words & c_words)
            if score > best_score:
                best_chunk, best_score, best_page = chunk, score, p

    return best_chunk, best_page

def ask_ai(question, context, page_no, model="qwen2.5:0.5b", host="http://localhost:11434"):
    body = json.dumps({
        "model": model,
        "stream": False,
        "options": {"temperature": 0.0},
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a strict reading comprehension assistant. Answer the question using ONLY the provided text excerpt. "
                    "CRITICAL: If the excerpt does NOT explicitly contain the answer, reply ONLY with: 'Not mentioned in the book.' "
                    "Do NOT use any outside knowledge or general facts. Answer in 1 short sentence."
                )
            },
            {
                "role": "user",
                "content": f"Text Excerpt from Book (Page {page_no}):\n\"{context}\"\n\nQuestion: {question}"
            }
        ]
    }).encode("utf-8")

    req = urllib.request.Request(f"{host}/api/chat", data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["message"]["content"]
    except urllib.error.URLError:
        return "Error: Could not reach Ollama. Make sure Ollama is running."

def run_query(question, model="qwen2.5:0.5b"):
    context, page = find_best_context(question)
    if not page or not context:
        print("No matching text found in the book.")
        return

    print(f"\n[Source: Book Page {page['book_page']} (PDF Page {page['pdf_page']})]")
    print(f"Context Excerpt: \"{context}\"")
    answer = ask_ai(question, context, page["book_page"], model=model)
    print(f"\nAI Answer: {answer}\n" + "-" * 70)

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    parser = argparse.ArgumentParser(description="Ask questions from Class 9 English Book")
    parser.add_argument("-q", "--question", help="Question to ask")
    parser.add_argument("--model", default="qwen2.5:0.5b", help="Ollama model name")
    args = parser.parse_args()

    if args.question:
        run_query(args.question, args.model)
        return

    print("Class 9 English Book Assistant (Zero-Hallucination)")
    print("Type your question below (or 'exit' to quit):\n")
    while True:
        try:
            q = input("Question> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("exit", "quit", "q"):
            break
        if q:
            run_query(q, args.model)

if __name__ == "__main__":
    main()
