import fitz
import re
import json

doc = fitz.open(r"c:\ds\mini_brightpath\English class 9.pdf")
print("Total pages in PDF:", len(doc))

SHIFTED_MARKERS = {'\x03', '\x0f', '\x10', '\x11', '\x1d', '\x87', '¿', '¶', 'µ', '±'}
SHIFTED_COMMON_WORDS = {'WKH', 'DQG', 'IRU', 'WR', 'RI', 'LV', 'DUH', 'ZDV', 'WKDW', 'WKLV', 'ZLWK', 'IURP', '8QLW', '1DPH', '3J', '1R', ',Q', 'SOD\\HG'}

def is_span_shifted(text):
    if any(m in text for m in SHIFTED_MARKERS):
        return True
    words = re.findall(r'[A-Za-z0-9,:\'¶µ±¿\\]+', text)
    if any(w in SHIFTED_COMMON_WORDS for w in words):
        return True
    return False

def clean_and_decode_span(text):
    if is_span_shifted(text):
        res = []
        for c in text:
            if c == ' ': res.append(' ')
            elif c == '\x03': res.append(' ')
            elif c == '\x0f': res.append(',')
            elif c == '\x10': res.append('-')
            elif c == '\x11': res.append('.')
            elif c == '\x1d': res.append(':')
            elif c == '\x87': res.append('•')
            elif c == 'µ': res.append('"')
            elif c == '¶': res.append("'")
            elif c == '¿': res.append('fi')
            elif c == '±': res.append('-')
            else:
                code = ord(c)
                if 1 <= code <= 93:
                    res.append(chr(code + 29))
                else:
                    res.append(c)
        return "".join(res)
    return text

def extract_clean_page(page):
    d = page.get_text("dict")
    raw_lines = []
    for b in d.get("blocks", []):
        if b.get("type") != 0:
            continue
        for l in b.get("lines", []):
            line_str = "".join(clean_and_decode_span(s["text"]) for s in l["spans"]).strip()
            if not line_str:
                continue
            # Filter headers & footers
            if re.match(r"^English\s*(Page\s*\d+)?$", line_str, re.I):
                continue
            if re.match(r"^Page\s*\d+$", line_str, re.I):
                continue
            if "indd" in line_str.lower() or re.match(r"^\d{2}-\d{2}-\d{4}", line_str):
                continue
            raw_lines.append(line_str)

    full_page = " ".join(raw_lines)
    # Extract embedded questions (e.g. • What did... ?)
    questions = re.findall(r'•\s*([^•\n\?]+\?)', full_page)
    # Remove the question bullets from the main story reading text
    clean_prose = re.sub(r'•\s*[^•\n\?]+\?', '', full_page)
    clean_prose = re.sub(r'\s+', ' ', clean_prose).strip()

    return clean_prose, [q.strip() for q in questions]

cleaned_book = []
for pno in range(8, len(doc)):
    prose, questions = extract_clean_page(doc[pno])
    if len(prose) > 40:
        cleaned_book.append({
            "pdf_page": pno + 1,
            "book_page": pno - 7,
            "text": prose,
            "questions": questions
        })

print(f"Extracted {len(cleaned_book)} cleaned pages!")

with open(r"c:\ds\mini_brightpath\cleaned_english_class9.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_book, f, indent=2, ensure_ascii=False)

print("Saved updated cleaned_english_class9.json with clean prose & questions separated!")
