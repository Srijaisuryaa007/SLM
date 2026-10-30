# BrightPath mini: fine-tune Qwen 2.5 0.5B on Google Colab (free T4 GPU)
#
# Steps
#   1. colab.research.google.com -> New notebook -> Runtime > Change runtime type > T4 GPU
#   2. Upload 2 files from this folder (left sidebar > Files):  train.jsonl  and  prompt.py
#   3. Copy each "# %%" block below into its own cell and run them in order
#
# Qwen 2.5 0.5B is chosen for mobile on-device apps: the exported Q4_K_M GGUF is only ~390 MB,
# well under the 1GB app size budget.

# %% Cell 1: install
# !pip install -q unsloth

# %% Cell 2: load Qwen 2.5 0.5B (4-bit) and add LoRA
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen2.5-0.5B-Instruct-bnb-4bit",
    max_seq_length=512,
    load_in_4bit=True
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=16,
    lora_dropout=0,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)

# %% Cell 3: turn each line of train.jsonl into text the model can read (Qwen ChatML format)
import json
from datasets import Dataset
from prompt import SYSTEM, make_message

rows = [json.loads(line) for line in open("train.jsonl", encoding="utf-8")]
texts = [
    f"<|im_start|>system\n{SYSTEM}<|im_end|>\n"
    f"<|im_start|>user\n{make_message(r['question'], r.get('info'))}<|im_end|>\n"
    f"<|im_start|>assistant\n{r['answer']}<|im_end|>\n"
    for r in rows
]
dataset = Dataset.from_dict({"text": texts})
print(len(rows), "examples. The first one:\n")
print(texts[0])

# %% Cell 4: train. Only the model's assistant response is learned from.
from trl import SFTConfig, SFTTrainer
from unsloth.chat_templates import train_on_responses_only

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    args=SFTConfig(
        dataset_text_field="text",
        max_seq_length=512,
        per_device_train_batch_size=2,
        num_train_epochs=5,
        learning_rate=2e-4,
        logging_steps=1,
        output_dir="outputs",
        report_to="none"
    )
)
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|im_start|>user\n",
    response_part="<|im_start|>assistant\n"
)
trainer.train()

# %% Cell 5: try it
FastLanguageModel.for_inference(model)

def ask(question, info=None):
    text = (
        f"<|im_start|>system\n{SYSTEM}<|im_end|>\n"
        f"<|im_start|>user\n{make_message(question, info)}<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    out = model.generate(**inputs, max_new_tokens=120, temperature=0.3, do_sample=True)
    return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

print(ask("I don't understand decimals."))
print(ask("What is the fee for Class 9 science?",
          "Class 9 Science: fee Rs 5000, 16 weeks, Tue Thu Sat 6:30 PM, teacher Dr. Meera Iyer."))
print(ask("Do you have a Class 11 chemistry course?"))

# %% Cell 6: export a lightweight .gguf file (~390 MB) for mobile app & Ollama
model.save_pretrained_gguf("brightpath_qwen_gguf", tokenizer, quantization_method="q4_k_m")
from google.colab import files
import glob
for f in glob.glob("brightpath_qwen_gguf*/*.gguf"):
    files.download(f)
