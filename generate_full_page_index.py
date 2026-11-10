import json
import re

with open('cleaned_english_class9.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

with open('mobile_app/assets/qa_bank.json', 'r', encoding='utf-8') as f:
    qa_bank = json.load(f)

# Map known questions from qa_bank by page
qa_by_page = {}
for item in qa_bank:
    p = str(item.get('page'))
    if p not in qa_by_page:
        qa_by_page[p] = []
    if item['question'] not in qa_by_page[p]:
        qa_by_page[p].append(item['question'])

def get_unit_for_page(page_no):
    if 1 <= page_no <= 27:
        return "Unit 1: Learning the Game / The Envious Neighbour"
    elif 28 <= page_no <= 56:
        return "Unit 2: I Can't Climb Trees Anymore"
    elif 57 <= page_no <= 85:
        return "Unit 3: Old Man River"
    elif 86 <= page_no <= 114:
        return "Unit 4: Seventeen Oranges / The Spider and the Fly"
    elif 115 <= page_no <= 122:
        return "Unit 5: Water – The Elixir of Life"
    else:
        return f"English Class 9 (Page {page_no})"

def extract_questions_from_page_text(text, page_no):
    found = []
    
    # 1. Add known questions from QA bank if present
    p_str = str(page_no)
    if p_str in qa_by_page:
        for q in qa_by_page[p_str]:
            found.append(q)

    # 2. Extract numbered questions/prompts: 1. ...? or 1. Without trust... or C. Answer...
    lines = [l.strip() for l in re.split(r'\n|(?<=[.!?])\s+', text) if l.strip()]
    for l in lines:
        # Match numbered exercises like "1. Without trust...", "2. What did...", "A. Choose..."
        if re.match(r'^(?:[0-9]{1,2}\.|\b[A-E]\.|\b[i|v|x]+\.)\s+[A-Z]', l):
            # Clean up line
            clean_l = l.strip()
            if len(clean_l) > 10 and clean_l not in found:
                # Truncate if too long
                if len(clean_l) > 110:
                    clean_l = clean_l[:108] + "..."
                found.append(clean_l)
        elif '?' in l and len(l) > 12:
            q_part = l[:l.index('?') + 1].strip()
            if len(q_part) > 10 and q_part not in found:
                if len(q_part) > 110:
                    q_part = q_part[:108] + "..."
                found.append(q_part)
        elif any(k in l.lower() for k in ['match the', 'fill in the', 'choose the correct']):
            clean_l = l.strip()
            if len(clean_l) > 10 and clean_l not in found:
                if len(clean_l) > 110:
                    clean_l = clean_l[:108] + "..."
                found.append(clean_l)

    # If still empty or only 1 item, generate page comprehension topics
    if len(found) == 0:
        found.append(f"Explain the key story events on Book Page {page_no}")
        found.append(f"What is the main topic discussed on Book Page {page_no}?")
        found.append(f"Read and summarize Book Page {page_no}")

    return found[:8] # Keep up to top 8 questions per page

full_page_index = {
    "units": [
        {"id": 1, "title": "Unit 1: Learning the Game", "pages": list(range(1, 28))},
        {"id": 2, "title": "Unit 2: I Can't Climb Trees Anymore", "pages": list(range(28, 57))},
        {"id": 3, "title": "Unit 3: Old Man River", "pages": list(range(57, 86))},
        {"id": 4, "title": "Unit 4: Seventeen Oranges / The Spider and the Fly", "pages": list(range(86, 115))},
        {"id": 5, "title": "Unit 5: Water – The Elixir of Life", "pages": list(range(115, 123))}
    ],
    "pages": {}
}

for p in pages:
    p_no = p.get('book_page')
    if not isinstance(p_no, int):
        continue
    txt = p.get('text', '')
    unit_name = get_unit_for_page(p_no)
    qs = extract_questions_from_page_text(txt, p_no)
    
    first_line = txt.strip().split('\n')[0][:50] if txt.strip() else f"Page {p_no} Content"
    
    full_page_index["pages"][str(p_no)] = {
        "unit": unit_name,
        "title": first_line,
        "questions": qs
    }

print(f"Generated complete directory for {len(full_page_index['pages'])} pages!")
print(f"Page 106 questions: {full_page_index['pages'].get('106', {}).get('questions')}")
print(f"Page 105 questions: {full_page_index['pages'].get('105', {}).get('questions')}")
print(f"Page 50 questions: {full_page_index['pages'].get('50', {}).get('questions')}")

with open('mobile_app/assets/page_index.json', 'w', encoding='utf-8') as f:
    json.dump(full_page_index, f, indent=2, ensure_ascii=False)

print("Saved updated mobile_app/assets/page_index.json successfully!")
