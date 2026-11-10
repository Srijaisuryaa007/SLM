import json
import re

with open('cleaned_english_class9.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} pages.")

cleaned_pages = []
for p in pages:
    txt = p['text']
    # Strip numbered in-text questions: e.g. "1. What did the visitor hide in the jackfruit tree? 2. ..."
    cleaned_txt = re.sub(r'\b\d+\.\s*[^0-9\n\?]+\?', ' ', txt)
    cleaned_txt = re.sub(r'•\s*[^•\n\?]+\?', ' ', cleaned_txt)
    cleaned_txt = re.sub(r'\b\d+\.\s*(?=\d+\.|$)', ' ', cleaned_txt)
    cleaned_txt = re.sub(r'\s+', ' ', cleaned_txt).strip()
    
    cleaned_pages.append({
        "pdf_page": p["pdf_page"],
        "book_page": p["book_page"],
        "text": cleaned_txt,
        "questions": p.get("questions", [])
    })

# Save updated cleaned_english_class9.json
with open('cleaned_english_class9.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_pages, f, indent=2, ensure_ascii=False)

# Save mobile_app/assets/facts.json
with open('mobile_app/assets/facts.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_pages, f, indent=2, ensure_ascii=False)

print("Saved cleaned pages to cleaned_english_class9.json and mobile_app/assets/facts.json!")
