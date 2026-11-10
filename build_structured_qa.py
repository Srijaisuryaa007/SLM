import json
import re

def make_qa(question, direct_answer, aliases, page, evidence, completed_sentence=None, matches=None, explanation=None):
    lines = [f"🎯 DIRECT ANSWER:\n**{direct_answer}**"]
    if matches:
        lines.append("\n📋 MATCH THE FOLLOWING:")
        for k, v in matches:
            lines.append(f"  • **{k}** ➔ **{v}**")
    elif completed_sentence:
        lines.append(f"\n📝 COMPLETED SENTENCE:\n\"{completed_sentence}\"")
    if explanation:
        lines.append(f"\n💡 EXPLANATION:\n{explanation}")
    lines.append(f"\n📖 PROOF & CITATION:\n  • **Book Page:** Page {page}\n  • **Textbook Quote:** \"{evidence}\"")
    
    formatted_answer = "\n".join(lines)
    
    return {
        "question": question,
        "aliases": aliases,
        "direct_answer": direct_answer,
        "completed_sentence": completed_sentence,
        "matches": matches,
        "explanation": explanation,
        "page": page,
        "evidence": evidence,
        "answer": formatted_answer
    }

qa_list = [
    # ==========================================
    # UNIT 1: Learning the Game (Sachin Tendulkar)
    # ==========================================
    make_qa(
        question="Match the words in column A with their synonym in column B (Unit 1)",
        direct_answer="Unit 1 Synonyms Matched",
        aliases=[
            "match the following unit 1",
            "match the following synonyms",
            "match synonyms unit 1",
            "match column a with column b unit 1",
            "match ease evolve excess survive immense",
            "synonyms match page 6"
        ],
        matches=[
            ("ease", "effortless"),
            ("evolve", "progress"),
            ("excess", "surplus"),
            ("survive", "endure"),
            ("immense", "great")
        ],
        page=6,
        evidence="Glossary & Vocabulary Exercise C: Match the words in column A with their synonym in column B."
    ),
    make_qa(
        question="Match the words in column A with their antonym in column B (Unit 1)",
        direct_answer="Unit 1 Antonyms Matched",
        aliases=[
            "match the following antonyms",
            "antonyms match page 6",
            "antonyms unit 1",
            "match concentrate inevitable occasional complete insane"
        ],
        matches=[
            ("concentrate", "distract"),
            ("inevitable", "preventable"),
            ("occasional", "continual"),
            ("complete", "incomplete"),
            ("insane", "wise")
        ],
        page=6,
        evidence="Vocabulary Exercise D: Match the words in column A with their antonym in column B."
    ),
    make_qa(
        question="Who was Sachin's coach?",
        direct_answer="Ramakant Achrekar Sir",
        aliases=[
            "who was sachins coach",
            "who was sachin coach",
            "who is sachins coach",
            "who is sachin coach",
            "coach of sachin",
            "who coached sachin",
            "sachin cricket coach",
            "achrekar sir"
        ],
        completed_sentence="Sachin's cricket coach was **Ramakant Achrekar Sir**.",
        explanation="Achrekar Sir ran summer cricket camps at Shivaji Park in Dadar, Mumbai.",
        page=1,
        evidence="Ramakant Achrekar Sir... was running the summer camp at Shivaji Park. Anyone who wanted to could come for a trial at the camp."
    ),
    make_qa(
        question="Who took Sachin to the cricket camp?",
        direct_answer="Ajit Tendulkar (Sachin's brother)",
        aliases=[
            "who took sachin to the camp",
            "who took sachin to cricket camp",
            "who took sachin to achrekar sir",
            "sachin brother",
            "who is ajit",
            "who was ajit"
        ],
        completed_sentence="Sachin's elder brother **Ajit** took him to Achrekar Sir's cricket camp.",
        explanation="Ajit spotted Sachin's natural batting talent and introduced him to Achrekar Sir.",
        page=1,
        evidence="My brother Ajit was the one who took me to Achrekar Sir for the first time."
    ),
    make_qa(
        question="Who were Sachin's favourite players?",
        direct_answer="Sunil Gavaskar and Viv Richards",
        aliases=[
            "who were sachins favourite players",
            "sachin favourite players",
            "favourite players of sachin",
            "who did sachin emulate",
            "who are sachin favorite players"
        ],
        completed_sentence="Sachin's favourite players were **Sunil Gavaskar and the West Indian legend Viv Richards**.",
        explanation="Sachin loved emulating their batting mannerisms in his early days.",
        page=1,
        evidence="I often tried to emulate the mannerisms of my favourite players, Sunil Gavaskar and the West Indian legend Viv Richards."
    ),
    make_qa(
        question="What did Sachin do during the thirty-minute break?",
        direct_answer="Ate a vadapav",
        aliases=[
            "thirty minute break",
            "what did sachin do during the break",
            "what did sachin eat during break",
            "sachin vadapav"
        ],
        completed_sentence="During the thirty-minute break between practice sessions, Sachin ate a **vadapav** with money given by Achrekar Sir.",
        page=3,
        evidence="During the break, Sir would often give me some money to go and have a vadapav (a popular Mumbai fast food)."
    ),
    make_qa(
        question="What was placed on top of the stumps in the last 15 minutes?",
        direct_answer="A One Rupee Coin",
        aliases=[
            "one rupee coin",
            "what happened with one rupee coin",
            "what was placed on top of stumps",
            "what was kept on stumps",
            "how many one rupee coins did sachin win"
        ],
        completed_sentence="Achrekar Sir placed a **one rupee coin** on top of the stumps for Sachin to defend.",
        explanation="If Sachin avoided getting out while every bowler bowled to him, the coin was his. He won 13 such coins.",
        page=3,
        evidence="Sir would place a one rupee coin on top of the stumps and if I managed to avoid getting out, the coin was mine."
    ),
    make_qa(
        question="Why did Sachin change his school to Shardashram Vidyamandir?",
        direct_answer="Shardashram Vidyamandir gave great importance to cricket",
        aliases=[
            "why did sachin change school",
            "why did sachin move to shardashram",
            "shardashram vidyamandir"
        ],
        completed_sentence="Sachin changed to **Shardashram Vidyamandir** because Achrekar Sir was the cricket coach there and the school prioritized cricket.",
        page=2,
        evidence="Achrekar Sir was the cricket coach at Shardashram Vidyamandir and the school gave great importance to cricket."
    ),
    make_qa(
        question="Who is Sachin Tendulkar?",
        direct_answer="Legendary Indian Cricketer & Bharat Ratna Awardee",
        aliases=[
            "who is sachin",
            "who is sachin tendulkar",
            "tell me about sachin tendulkar",
            "sachin tendulkar",
            "about sachin"
        ],
        completed_sentence="**Sachin Ramesh Tendulkar** is a former Indian cricketer, widely regarded as one of the greatest batsmen in cricket history.",
        explanation="He played 664 international matches, scored 34,357 runs, and was awarded the Bharat Ratna in 2014.",
        page=4,
        evidence="Sachin Ramesh Tendulkar was born on 24 April 1973 in Bombay, Maharashtra. He is a former Indian cricketer and captain, widely regarded as one of the greatest cricketers of all time."
    ),

    # ==========================================
    # UNIT 2: I Can't Climb Trees Anymore (Ruskin Bond)
    # ==========================================
    make_qa(
        question="Match the words in column A with the meanings in column B (Unit 2)",
        direct_answer="Unit 2 Vocabulary Meanings Matched",
        aliases=[
            "match the following unit 2",
            "match the following page 33",
            "match words in column a with meanings in column b",
            "match the following pruning chiming drenched",
            "match pruning chiming drenched dizzy prosperous sprightliness treasure rusty",
            "pruning chiming drenched match"
        ],
        matches=[
            ("pruning", "the act of trimming a plant"),
            ("chiming", "making melodious ringing sounds (indicating time)"),
            ("drenched", "soaked thoroughly"),
            ("dizzy", "unsteady or shaky"),
            ("prosperous", "flourishing and thriving"),
            ("sprightliness", "lively and full of energy"),
            ("treasure", "a collection of precious things"),
            ("rusty", "ancient or covered in rust")
        ],
        page=33,
        evidence="Unit 2 Exercise D: Match the words in column A with the meanings in column B by drawing a line."
    ),
    make_qa(
        question="The visitor gifted the _________ to the little girl.",
        direct_answer="iron cross (Option a)",
        aliases=[
            "the visitor gifted the to the little girl",
            "the visitor gifted the blank to the little girl",
            "visitor gifted the blank to little girl",
            "what did the visitor gift to the little girl",
            "what did the visitor gift to the girl",
            "visitor gifted what to girl",
            "the visitor gifted the",
            "visitor gifted"
        ],
        completed_sentence="The visitor gifted the **iron cross** to the little girl.",
        explanation="He placed the German Iron Cross medal in her hands because she climbed the jackfruit tree and retrieved it for him.",
        page=33,
        evidence="‘On the right day, at the right time, and with the right person’, he said, getting up and placing the medal in her hands."
    ),
    make_qa(
        question="What did the visitor hide in the jackfruit tree?",
        direct_answer="An Iron Cross, marbles, an unread book, and old coins",
        aliases=[
            "what did the visitor hide in the jackfruit tree",
            "what did he hide in the jackfruit tree",
            "what did the visitor keep in the jackfruit tree",
            "what was hidden in the jackfruit tree",
            "what did he leave in the jackfruit tree",
            "what treasures did the visitor keep in the tree",
            "what did visitor hide in jackfruit tree",
            "visitor hide jackfruit tree"
        ],
        completed_sentence="The visitor hid his childhood treasures—**marbles, an unread book, old coins, and his grandfather's Iron Cross**—in the hollow of the jackfruit tree.",
        page=30,
        evidence="Half way along it there’s a small hollow in which I used to keep some of my treasures... Marbles I’d won. A book I wasn’t supposed to read. A few old coins I’d collected... There was my grandfather’s Iron Cross... I left it in the jackfruit tree."
    ),
    make_qa(
        question="The story 'I Can't Climb Trees Anymore' highlights the importance of _________.",
        direct_answer="youth (Option b)",
        aliases=[
            "the story i cant climb trees anymore highlights the importance of",
            "the story highlights the importance of",
            "story highlights importance of blank",
            "highlights the importance of youth",
            "importance of youth"
        ],
        completed_sentence="The story 'I Can't Climb Trees Anymore' highlights the importance of **youth**.",
        explanation="The visitor realized that he did not return for the house or the Iron Cross, but to relive his memories of youth.",
        page=32,
        evidence="‘It wasn’t the Cross I came for. It was my youth.’"
    ),
    make_qa(
        question="The old house was built with _________.",
        direct_answer="solid blocks of granite",
        aliases=[
            "the old house was built with",
            "the house was built with",
            "what was the old house built with",
            "how was the old house built",
            "the old house was built with blank"
        ],
        completed_sentence="The old house was built with **solid blocks of granite**.",
        page=28,
        evidence="The old house built with solid blocks of granite wasn’t altered at all."
    ),
    make_qa(
        question="The house which was visited by the man _________.",
        direct_answer="remained unchanged (Option a)",
        aliases=[
            "the house which was visited by the man",
            "the house visited by the man"
        ],
        completed_sentence="The house visited by the man **remained unchanged**.",
        page=32,
        evidence="The old house built with solid blocks of granite wasn’t altered at all."
    ),
    make_qa(
        question="The visitor came back to the house because he _________.",
        direct_answer="was looking for his lost youth (Option b)",
        aliases=[
            "the visitor came back to the house because he",
            "why did the visitor come back to the house",
            "why did he return to the house"
        ],
        completed_sentence="The visitor returned to the house because he **was looking for his lost youth**.",
        page=33,
        evidence="‘It wasn’t the Cross I came for. It was my youth. And you can’t buy back your youth.’"
    ),
    make_qa(
        question="Who said, 'A blessing rests on the house where the shadow of a tree falls'?",
        direct_answer="The visitor's grandmother",
        aliases=[
            "a blessing rests on the house where the shadow of a tree falls",
            "who said a blessing rests on the house",
            "blessing rests on the house"
        ],
        completed_sentence="**The visitor's grandmother** said that a blessing rests on the house where the shadow of a tree falls.",
        page=28,
        evidence="He remembered his grandmother saying: ‘A blessing rests on the house where the shadow of a tree falls.’"
    ),
    make_qa(
        question="Does the visitor still live in the house?",
        direct_answer="No, his family sold it twenty-five years ago",
        aliases=[
            "does the visitor still live in the house",
            "did the visitor live in the house",
            "when did he sell the house",
            "twenty five years ago"
        ],
        completed_sentence="**No**, the visitor does not live in the house; his family sold it **twenty-five years ago** after his grandmother died.",
        page=29,
        evidence="‘No, I used to live here twenty-five years ago. As a boy. As a young man.... And then my grandmother died, and we sold the house and went away.’"
    ),
    make_qa(
        question="Who wrote 'I Can't Climb Trees Anymore'?",
        direct_answer="Ruskin Bond",
        aliases=[
            "who wrote i cant climb trees anymore",
            "author of i cant climb trees anymore",
            "who is ruskin bond",
            "ruskin bond",
            "about ruskin bond"
        ],
        completed_sentence="The story 'I Can't Climb Trees Anymore' was written by **Ruskin Bond**.",
        explanation="He is an award-winning Indian author of British descent, known for promoting children's literature in India.",
        page=31,
        evidence="Ruskin Bond was born on 19th May 1934. He is an award winning Indian author of British descent. He is much renowned for his role in promoting children’s literature in India."
    ),

    # ==========================================
    # UNIT 4: Seventeen Oranges (Bill Naughton)
    # ==========================================
    make_qa(
        question="Match the phrasal verbs in Column A with their meanings in Column B (Unit 4)",
        direct_answer="Unit 4 Phrasal Verbs Matched",
        aliases=[
            "match the following unit 4",
            "phrasal verbs match unit 4",
            "match column a column b seventeen oranges",
            "match fond of hidden away lock up laughed at look at bring up gave up went through finish off figure out"
        ],
        matches=[
            ("fond of", "having a liking for"),
            ("hidden away", "kept concealed in a secret place"),
            ("lock up", "confine someone in a cell / prison"),
            ("laughed at", "mocked or ridiculed"),
            ("look at", "observe or inspect carefully"),
            ("bring up", "raise or mention a matter"),
            ("gave up", "abandoned or surrendered"),
            ("went through", "searched thoroughly / experienced"),
            ("finish off", "consume or destroy entirely"),
            ("figure out", "understand or solve")
        ],
        page=97,
        evidence="Unit 4 Grammar Exercise A: Given below in Column A are some phrasal verbs taken from the text. Find the meanings by using a dictionary and complete Column B."
    ),
    make_qa(
        question="Where did the narrator work in Seventeen Oranges?",
        direct_answer="Swift Delivery Company (at the docks)",
        aliases=[
            "where did the narrator work",
            "where did the narrator work in seventeen oranges",
            "what was the narrators job in the docks",
            "swift delivery company",
            "narrator job"
        ],
        completed_sentence="The narrator worked driving a pony and cart for the **Swift Delivery Company** carrying goods to and from the docks.",
        page=88,
        evidence="I drove a pony and cart for the Swift Delivery Company. We carried goods to and from the docks."
    ),
    make_qa(
        question="The narrator was very fond of _________.",
        direct_answer="eating oranges (Option c)",
        aliases=[
            "the narrator was very fond of",
            "narrator fond of blank",
            "the narrator was very fond of blank"
        ],
        completed_sentence="The narrator was very fond of **eating oranges**.",
        page=93,
        evidence="Oranges. I was fond of them. I used to eat them all day and every day."
    ),
    make_qa(
        question="The narrator was searched by the policeman, because _________.",
        direct_answer="his pockets were bulging (Option d)",
        aliases=[
            "the narrator was searched by the policeman because",
            "why was the narrator searched",
            "why did pongo search the narrator"
        ],
        completed_sentence="The narrator was searched by policeman Pongo because **his pockets were bulging**.",
        page=93,
        evidence="Pongo stopped me. ‘Wait a minute,’ he said. He looked into my face. ‘What’s that you’ve got in your pockets?’... ‘Let’s have a look.’"
    ),
    make_qa(
        question="The narrator kept his mouth shut when questioned by Pongo, because _________.",
        direct_answer="anything said would be held as evidence against him (Option a)",
        aliases=[
            "the narrator kept his mouth shut",
            "why did the narrator keep his mouth shut",
            "kept his mouth shut when questioned by pongo"
        ],
        completed_sentence="The narrator kept his mouth shut because **anything said would be held as evidence against him**.",
        page=93,
        evidence="I said nothing. I had read a lot of detective stories, and I knew that the best thing was to keep quiet. Anything you say may be used as evidence against you."
    ),
    make_qa(
        question="The voice in the narrator's head advised him to _________.",
        direct_answer="eat all the oranges (Option b)",
        aliases=[
            "the voice in the narrators head advised him to",
            "what did the voice advise him to do",
            "voice in head advised"
        ],
        completed_sentence="The inner voice in the narrator's head advised him to **eat all seventeen oranges**, including pips and peels.",
        page=93,
        evidence="‘Eat them,’ said the voice in my head. ‘Eat the evidence.’"
    ),
    make_qa(
        question="Pongo found no trace of the oranges on the table, because _________.",
        direct_answer="the narrator had eaten them all (Option c)",
        aliases=[
            "pongo found no trace of the oranges",
            "why did pongo find no trace of oranges",
            "no trace of oranges on table"
        ],
        completed_sentence="Policeman Pongo found no trace of the oranges because **the narrator had eaten and swallowed them all**.",
        page=93,
        evidence="‘Where are the oranges?’ asked Pongo. ‘I can smell them.’ But there was not a trace of an orange anywhere."
    ),
    make_qa(
        question="What was Clem Jones carrying in the box?",
        direct_answer="A ship's cat",
        aliases=[
            "what was clem jones carrying in the box",
            "clem jones box",
            "clem jones was carrying a blank in the box",
            "what did clem jones carry",
            "clem jones cat"
        ],
        completed_sentence="Clem Jones was carrying a **ship's cat** inside the box.",
        explanation="When the policeman forced him to open the box, the ginger cat leapt out and ran back to the docks.",
        page=89,
        evidence="When the policeman opened it, a big ginger cat bounded out and ran back towards the docks."
    ),
    make_qa(
        question="What did the narrator do with the seventeen oranges?",
        direct_answer="Swallowed all 17 oranges with pips and peels",
        aliases=[
            "what did the narrator do with the oranges",
            "what did the narrator do with the seventeen oranges",
            "what did the narrator do with the pips and peels",
            "how did he eat seventeen oranges",
            "swallowed the evidence"
        ],
        completed_sentence="The narrator **ate and swallowed all seventeen oranges**, including the pips and peel, destroying all evidence.",
        page=91,
        evidence="I ate the lot: flesh, pips, and peel. I had swallowed the evidence, all seventeen oranges."
    ),

    # ==========================================
    # UNIT 5: Water – The Elixir of Life (Sir C.V. Raman)
    # ==========================================
    make_qa(
        question="The real elixir of life according to Sir C.V. Raman is _________.",
        direct_answer="plain water",
        aliases=[
            "the real elixir of life according to sir cv raman is",
            "what is the real elixir of life",
            "real elixir of life blank",
            "what is the true elixir of life",
            "real elixir of life"
        ],
        completed_sentence="According to Sir C.V. Raman, the real elixir of life is **plain water**.",
        page=118,
        evidence="Man has through the ages sought in vain for an imaginary elixir of life... but the true elixir lies near to our hands. For of all substances, water is the most common and the most wonderful."
    ),
    make_qa(
        question="Water in a landscape is compared to the _________ in a human face.",
        direct_answer="eyes",
        aliases=[
            "water in a landscape is compared to the",
            "water in a landscape is compared to blank",
            "what does the writer compare water in a landscape to",
            "compared to the eyes in a human face",
            "water in a landscape"
        ],
        completed_sentence="Water in a landscape is compared to the **eyes** in a human face.",
        explanation="It reflects the mood of the hour, being bright and gay when the sun shines, and dark and gloomy when overcast.",
        page=118,
        evidence="Water in a landscape may be compared to the eyes in a human face. It reflects the mood of the hour, being bright and gay when the sun shines, turning to dark and gloomy when the sky is overcast."
    ),
    make_qa(
        question="What is the 'cheering sight' mentioned in Water – The Elixir of Life?",
        direct_answer="The rainfed tanks of South India when full",
        aliases=[
            "what is the cheering sight",
            "what is the cheering sight mentioned in the paragraph",
            "cheering sight water elixir of life",
            "rainfed tanks south india"
        ],
        completed_sentence="The cheering sight is the **rainfed tanks of South India** when they are full of water.",
        explanation="These tanks play a vital role in South Indian agriculture and look beautiful at sunrise or sunset.",
        page=118,
        evidence="The rainfed tanks that are so common in South India – Alas! often so sadly neglected in their maintenance – are a cheering sight when they are full."
    ),
    make_qa(
        question="What is the imaginary elixir of life?",
        direct_answer="The divine Amrita / elixir of life sought in vain",
        aliases=[
            "what is the imaginary elixir of life",
            "imaginary elixir of life",
            "divine amrita"
        ],
        completed_sentence="The imaginary elixir of life is the **divine Amrita** which man sought in vain to confer immortality.",
        page=118,
        evidence="Man has through the ages sought in vain for an imaginary elixir of life, the divine Amrita, a draught of which was thought to confer immortality."
    ),
    make_qa(
        question="Egypt was made by which river?",
        direct_answer="River Nile",
        aliases=[
            "egypt was made by which river",
            "which river made egypt",
            "river nile",
            "egypt and nile"
        ],
        completed_sentence="Egypt was made by the **River Nile**, brought down by flood waters from the highlands of Abyssinia and Central Africa.",
        page=118,
        evidence="Egypt, in fact, was made by its river. Its ancient civilization was created and is sustained by the life-giving waters which come down year after year with unfailing regularity."
    ),

    # ==========================================
    # Supplementary: The Envious Neighbour (Unit 1)
    # ==========================================
    make_qa(
        question="The old farmer and his wife loved the dog _________.",
        direct_answer="as if it was their own baby (Option b)",
        aliases=[
            "the old farmer and his wife loved the dog",
            "how did the old farmer and wife love the dog"
        ],
        completed_sentence="The old farmer and his wife loved the dog **as if it was their own baby**.",
        page=25,
        evidence="The old farmer and his wife loved the dog as if it was their own baby."
    ),
    make_qa(
        question="When the old couple became rich, they _________.",
        direct_answer="lived a comfortable life and were generous towards poor neighbours (Option c)",
        aliases=[
            "when the old couple became rich they",
            "old couple became rich"
        ],
        completed_sentence="When the old couple became rich, they **lived a comfortable life and were generous towards their poor neighbours**.",
        page=25,
        evidence="The good old couple became rich, bought themselves a piece of land, gave to the poor, and lived in comfort."
    )
]

print(f"Generated {len(qa_list)} structured Q&A items.")

with open('textbook_qa.json', 'w', encoding='utf-8') as f:
    json.dump(qa_list, f, indent=2, ensure_ascii=False)

with open('mobile_app/assets/qa_bank.json', 'w', encoding='utf-8') as f:
    json.dump(qa_list, f, indent=2, ensure_ascii=False)

print("Saved textbook_qa.json and mobile_app/assets/qa_bank.json successfully!")
