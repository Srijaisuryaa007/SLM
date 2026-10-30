# BrightPath mini: Mobile SLM Edition (< 1 GB)

A tiny, complete example of an on-device Small Language Model (SLM) for mobile apps that:
1. Answers in an educational company's friendly style (via **Qwen 2.5 0.5B Instruct**).
2. Looks up live company facts on-device without retraining (via **local keyword RAG** on `facts.json`).
3. Keeps total application download size under **~425 MB** (well below the 1 GB mobile limit).

## The idea in one picture

```
 Student (Mobile App): "What is the fee for Class 9 science?"
        |
   1. FIND    on-device search of facts.json for matching fact
        |        -> "Class 9 Science: fee Rs 5000, 16 weeks, ..."
   2. BUILD   construct Qwen ChatML prompt with fact + question
        |        -> "<|im_start|>user\nInfo: Class 9 Science ... Question: ...<|im_end|>"
   3. ASK     on-device Qwen 2.5 0.5B GGUF generates answer
        |
 "The fee for Class 9 Science is Rs 5000 for 16 weeks. Quick check: Would you like the teacher's name or timings?"
```

## Project Structure

| File / Folder | What it is |
|---|---|
| [`facts.json`](facts.json) | Company knowledge base (courses, fees, policies) |
| [`train.jsonl`](train.jsonl) | 14 practice training examples |
| [`prompt.py`](prompt.py) | System rules and message layout |
| [`ask.py`](ask.py) | CLI testing tool |
| [`finetune_colab.py`](finetune_colab.py) | Fine-tunes Qwen 2.5 0.5B on Colab and exports ~390MB GGUF |
| [`Modelfile`](Modelfile) | Ollama packaging config for Qwen ChatML format |
| [`mobile_app/`](mobile_app/) | **The Mobile App**: React Native offline app + instant browser preview |

## Quick Testing

1. **Test in CLI with Qwen 2.5 0.5B:**
   ```bash
   python ask.py --model qwen2.5:0.5b -q "What is the fee for Class 9 science?"
   ```

2. **Test Mobile Handset UI in Browser:**
   Open [`mobile_app/mobile_preview.html`](mobile_app/mobile_preview.html) in your browser. It features a complete mobile device preview with verified fact badges and streaming responses.
