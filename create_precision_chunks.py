import json
import re

with open('cleaned_english_class9.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

STOP = set("a an the is are was were of for to in on at and or do does did i my me you your what whats how can could when who whom which where there it be been with about tell please much many have has had will would if any get this that these those from by".split())

def clean_text(txt):
    # Remove raw multiple choice questions lines or exercise artifacts that corrupt reading prose
    lines = []
    for line in txt.split('\n'):
        l = line.strip()
        if not l:
            continue
        if re.match(r'^[a-e]\)\s+', l):
            continue
        if l.startswith("Ans:") or l.startswith("Q."):
            continue
        lines.append(l)
    return " ".join(lines)

chunks = []

def determine_unit_info(page_no, text_sample):
    t = text_sample.lower()
    if page_no <= 7:
        return 1, "Unit 1: Learning the Game", "sachin_cricket", "Prose", ["sachin", "cricket", "achrekar", "ajit", "shivaji", "shardashram", "vadapav", "gavaskar", "stumps", "nets"]
    elif page_no <= 18:
        return 1, "Unit 1: A Poison Tree", "poison_tree", "Poem", ["poison", "tree", "blake", "wrath", "anger", "foe", "apple", "garden"]
    elif page_no <= 27:
        return 1, "Unit 1: The Envious Neighbour", "envious_neighbour", "Supplementary", ["neighbour", "dog", "shiro", "ashes", "cherry", "blossom", "pine", "mortar"]
    elif page_no <= 36:
        return 2, "Unit 2: I Can't Climb Trees Anymore", "ruskin_tree", "Prose", ["visitor", "ruskin", "bond", "jackfruit", "tree", "cross", "granite", "climb", "grandmother", "turnstile"]
    elif page_no <= 43:
        return 2, "Unit 2: On Killing a Tree", "killing_tree", "Poem", ["tree", "gieve", "patel", "bark", "hack", "chop", "root", "earth"]
    elif page_no <= 56:
        return 2, "Unit 2: The Fun They Had", "fun_they_had", "Supplementary", ["margie", "tommy", "mechanical", "teacher", "county", "inspector", "telebook", "school", "2157"]
    elif page_no <= 69:
        return 3, "Unit 3: Old Man River", "old_man_river", "Drama", ["river", "flood", "amy", "betty", "rose", "sara", "jim", "peters", "marsh", "red", "cross", "cloudburst", "splint", "ladder"]
    elif page_no <= 76:
        return 3, "Unit 3: The River", "the_river", "Poem", ["river", "caroline", "bowles", "pebble", "dancing", "ocean", "swelling"]
    elif page_no <= 85:
        return 3, "Unit 3: Earthquake", "earthquake", "Supplementary", ["earthquake", "brij", "bhukki", "mahadevan", "pauri", "garhwal", "officer", "rubble"]
    elif page_no <= 98:
        return 4, "Unit 4: Seventeen Oranges", "seventeen_oranges", "Prose", ["oranges", "seventeen", "pongo", "clem", "jones", "cat", "box", "cheese", "docks", "steal", "pips", "peel", "apron", "pocket"]
    elif page_no <= 107:
        return 4, "Unit 4: The Spider and the Fly", "spider_fly", "Poem", ["spider", "fly", "parlour", "web", "gauzy", "wings", "eyes", "flattery", "cunning", "trust", "betray", "den"]
    elif page_no <= 114:
        return 4, "Unit 4: The Cat and the Pain-Killer", "cat_painkiller", "Supplementary", ["cat", "painkiller", "pain-killer", "peter", "aunt", "polly", "tom", "sawyer", "becky", "thimble", "somersaults", "window"]
    else:
        return 5, "Unit 5: Water – The Elixir of Life", "water_elixir", "Prose", ["water", "elixir", "raman", "nile", "egypt", "silt", "soil", "erosion", "rainfed", "tanks", "amrita"]

chunk_idx = 1
for p in pages:
    page_no = p.get('book_page')
    if not isinstance(page_no, int):
        continue
    raw_text = p.get('text', '')
    if not raw_text.strip():
        continue

    cleaned = clean_text(raw_text)
    unit_id, unit_title, topic_code, lesson_type, default_kw = determine_unit_info(page_no, cleaned)

    # Split text into natural sentences
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', cleaned) if len(s.strip()) > 15]
    if not sentences:
        continue

    # Window of 2-4 sentences with 1-2 sentence overlap for maximum context preservation
    step = 2
    window = 4
    for i in range(0, len(sentences), step):
        batch = sentences[i:i+window]
        if not batch:
            continue
        chunk_text = " ".join(batch)
        if len(chunk_text.split()) < 15:
            continue

        raw_words = re.findall(r'[a-z0-9]+', chunk_text.lower())
        meaningful_words = list(set([w for w in raw_words if w not in STOP and len(w) > 2]))
        
        all_kw = list(set(default_kw + meaningful_words))

        chunks.append({
            "id": f"chunk_{chunk_idx:04d}",
            "unit": unit_id,
            "unit_title": unit_title,
            "topic": topic_code,
            "lesson_type": lesson_type,
            "page": page_no,
            "text": chunk_text,
            "keywords": all_kw
        })
        chunk_idx += 1

print(f"Total textbook chunks created: {len(chunks)}")

# Verify distribution across topics
topic_counts = {}
for ch in chunks:
    topic_counts[ch['topic']] = topic_counts.get(ch['topic'], 0) + 1
for top, count in topic_counts.items():
    print(f"  Topic {top:20s}: {count:3d} chunks")

with open('mobile_app/assets/chunks.json', 'w', encoding='utf-8') as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)
print("Saved to mobile_app/assets/chunks.json!")
