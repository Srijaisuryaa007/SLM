import json
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def sanitize_xml(text):
    if not text: return ""
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

# Load cleaned pages
with open(r"c:\ds\mini_brightpath\cleaned_english_class9.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

doc = Document()

# Set page margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Title
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_run = title_p.add_run("English Standard IX - Cleaned Textbook & Grounded Q&A")
title_run.font.size = Pt(20)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(24, 76, 120)

sub_p = doc.add_paragraph()
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_run = sub_p.add_run("Processed from page VIII onwards | Noise, Headers & Footers Removed | AI Grounded Answers")
sub_run.font.size = Pt(10)
sub_run.font.italic = True
sub_run.font.color.rgb = RGBColor(100, 100, 100)

doc.add_paragraph()

# Add a showcase of Grounded Q&A first
qa_heading = doc.add_heading("Part 1: Key Book Questions & Grounded AI Answers", level=1)
qa_heading.style.font.color.rgb = RGBColor(24, 76, 120)

sample_qa = [
    {
        "page": 1,
        "question": "Who were Sachin's favourite players?",
        "answer": "Sachin Tendulkar's favourite players were Sunil Gavaskar and the West Indian legend Viv Richards.",
        "evidence": "I often tried to emulate the mannerisms of my favourite players, Sunil Gavaskar and the West Indian legend Viv Richards."
    },
    {
        "page": 1,
        "question": "What was special about Shardashram Vidyamandir in Mumbai?",
        "answer": "Ramakant Achrekar Sir was the cricket coach at Shardashram Vidyamandir, and the school gave great importance to the game of cricket.",
        "evidence": "Achrekar Sir ran summer camps too. Ajit, my brother, brought me to him... the school gave cricket supreme priority."
    },
    {
        "page": 2,
        "question": "What routine did Sachin follow in washing his clothes?",
        "answer": "Sachin only had one set of cricket clothes, so he washed them as soon as he returned from the morning session and hung them to dry while he ate lunch, often playing the evening session in wet pockets.",
        "evidence": "There was never quite enough time for the pockets to dry out completely, and for the entire duration of the camp I played with wet pockets."
    },
    {
        "page": 2,
        "question": "What suggestion did Achrekar Sir give to Sachin's father?",
        "answer": "Achrekar Sir informed Sachin's father that Sachin had the potential to be a good cricketer and suggested moving him to Shardashram Vidyamandir where he could practice all year round.",
        "evidence": "Sir informed Ajit that I had the potential to be a good cricketer if I practiced all year round... Achrekar Sir was keen for me to change schools."
    },
    {
        "page": 3,
        "question": "What did Sachin do during the thirty-minute break?",
        "answer": "During the thirty-minute break, Achrekar Sir would give Sachin money to go and eat a vadapav, a popular Mumbai fast food.",
        "evidence": "During the break, Sir would often give me some money to go and have a vadapav (a popular Mumbai fast food)."
    },
    {
        "page": 3,
        "question": "What happened during the last 15 minutes of net practice with the one rupee coin?",
        "answer": "Sir placed a one rupee coin on top of the stumps, and every bowler in the camp bowled to Sachin; if Sachin survived without getting out, the coin was his.",
        "evidence": "Sir would place a one rupee coin on top of the stumps and if I managed to avoid getting out, the coin was mine. In this session every bowler in the camp would come and bowl to me."
    }
]

for item in sample_qa:
    qp = doc.add_paragraph()
    q_label = qp.add_run(f"Q (Page {item['page']}): ")
    q_label.bold = True
    q_label.font.color.rgb = RGBColor(180, 40, 40)
    qp.add_run(item['question'])

    ap = doc.add_paragraph()
    a_label = ap.add_run("Grounded AI Answer: ")
    a_label.bold = True
    a_label.font.color.rgb = RGBColor(30, 130, 60)
    ap.add_run(item['answer'])

    ep = doc.add_paragraph()
    e_label = ep.add_run("Textbook Evidence: ")
    e_label.italic = True
    e_label.font.size = Pt(9.5)
    e_label.font.color.rgb = RGBColor(90, 90, 90)
    e_text = ep.add_run(f'"{item["evidence"]}"')
    e_text.italic = True
    e_text.font.size = Pt(9.5)
    e_text.font.color.rgb = RGBColor(90, 90, 90)

    doc.add_paragraph() # Spacing

doc.add_page_break()

# Part 2: Cleaned Textbook Content
content_heading = doc.add_heading("Part 2: Cleaned English Textbook Content", level=1)
content_heading.style.font.color.rgb = RGBColor(24, 76, 120)

for p in pages:
    p_header = doc.add_paragraph()
    p_run = p_header.add_run(f"Book Page {p['book_page']} (PDF Page {p['pdf_page']})")
    p_run.bold = True
    p_run.font.size = Pt(11)
    p_run.font.color.rgb = RGBColor(70, 70, 150)

    p_body = doc.add_paragraph()
    p_body.paragraph_format.line_spacing = 1.15
    clean_txt = sanitize_xml(p['text'])
    p_body_run = p_body.add_run(clean_txt)
    p_body_run.font.size = Pt(10)

output_path = r"c:\ds\mini_brightpath\English_Class_9_Cleaned_Document.docx"
doc.save(output_path)
print(f"Successfully generated clean Word Document: {output_path}!")
