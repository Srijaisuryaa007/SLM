"""Ask the BrightPath mini assistant a question.

    python ask.py                                  chat
    python ask.py -q "What is the fee for Class 9 science?"
    python ask.py --model gemma2:2b                use the base model (before fine-tuning)

What happens for every question:
    1. FIND   the matching fact in facts.json (count shared words)
    2. BUILD  one message: the fact + the question
    3. ASK    the model in Ollama, which reads only that message
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

from prompt import SYSTEM, make_message

FACTS = json.loads((Path(__file__).parent / "facts.json").read_text(encoding="utf-8"))

# Small filler words that say nothing about the topic
STOP = set("a an the is are was of for to in on at and or do does i my me you your what whats how "
           "can when who which there it be with about tell please much many have has will if any get "
           "this that".split())


def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP


def find_fact(question, facts=FACTS):
    """Return the fact sharing the most words with the question, or None."""
    q = words(question)
    numbers = {w for w in q if w.isdigit()}
    best, best_score = None, 0
    for fact in facts:
        w = words(fact["text"])
        if not numbers <= w:        # asked about "Class 12" but the fact has no 12: skip it
            continue
        score = len(q & w)
        if score > best_score:
            best, best_score = fact, score
    return best


def ask_ollama(question, info, model, host="http://localhost:11434"):
    body = json.dumps({
        "model": model,
        "stream": False,
        "options": {"temperature": 0.3},
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": make_message(question, info)},
        ],
    }).encode("utf-8")
    req = urllib.request.Request(f"{host}/api/chat", data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read().decode("utf-8"))["message"]["content"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Model '{model}' not found. Run 'ollama list' to see your models."
        return f"Ollama error: {e}"
    except urllib.error.URLError:
        return "Could not reach Ollama. Start the Ollama app, then try again."


def run(question, model):
    fact = find_fact(question)
    info = fact["text"] if fact else None
    print(f"\n1) FIND   : {info if info else 'no fact matched'}")
    print("2) BUILD  : message sent to the model:")
    print("   " + make_message(question, info).replace("\n", "\n   "))
    print("3) ASK    :", ask_ollama(question, info, model))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # so emoji print on Windows
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="BrightPath mini assistant")
    ap.add_argument("-q", "--question")
    ap.add_argument("--model", default="brightpath-mini")
    args = ap.parse_args()
    if args.question:
        run(args.question, args.model)
        return
    print("BrightPath mini (type 'exit' to quit)")
    while True:
        try:
            q = input("\nStudent> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("exit", "quit"):
            break
        if q:
            run(q, args.model)


if __name__ == "__main__":
    main()
