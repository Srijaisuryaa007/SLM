import json

# Comprehensive Q&A with Structured MCQ Options (a, b, c, d)
# Every question from the textbook with options has:
# - options: [{"letter": "a", "text": "..."}, {"letter": "b", "text": "..."}, ...]
# - correct_option: "b"
# - direct_answer: "Option b) <text>"

qa_list = [
    {
        "page": 1,
        "question": "Who was Sachin's coach?",
        "aliases": [
            "who was sachins coach",
            "sachin coach",
            "coach of sachin",
            "who coached sachin",
            "name of sachins coach",
            "ramakant achrekar",
            "achrekar coach"
        ],
        "direct_answer": "Ramakant Achrekar Sir",
        "completed_sentence": "Sachin's cricket coach was **[Ramakant Achrekar Sir]** at Shivaji Park, Mumbai.",
        "explanation": "According to the textbook, Ramakant Achrekar was a dedicated cricket coach who ran summer camps at Shivaji Park and trained young Sachin.",
        "evidence": "My induction into the Mumbai cricket circuit could have ended in failure – but for Ajit’s insistence... Achrekar Sir was running summer camps at Shivaji Park."
    },
    {
        "page": 1,
        "question": "Who took Sachin to the cricket camp?",
        "aliases": [
            "who took sachin to the camp",
            "who took sachin to cricket camp",
            "who introduced sachin to achrekar",
            "who was ajit",
            "ajit tendulkar",
            "sachin brother"
        ],
        "direct_answer": "Ajit Tendulkar (Sachin's brother)",
        "completed_sentence": "Sachin was taken to Achrekar Sir's cricket camp by his elder brother **[Ajit Tendulkar]**.",
        "explanation": "According to the textbook, Ajit noticed Sachin's natural batting talent and convinced Achrekar Sir to give him a trial.",
        "evidence": "My brother Ajit was the one who spotted my potential and took me to Achrekar Sir's summer camp."
    },
    {
        "page": 1,
        "question": "Who were Sachin's favourite players?",
        "aliases": [
            "who were sachins favourite players",
            "sachin idol",
            "favourite players of sachin",
            "sachin role models",
            "gavaskar and richards"
        ],
        "direct_answer": "Sunil Gavaskar and Viv Richards",
        "completed_sentence": "Sachin's favourite international cricketers were **[Sunil Gavaskar and Sir Viv Richards]**.",
        "explanation": "According to the book, Sachin idolized Sunil Gavaskar's immaculate technique and Viv Richards' aggressive style.",
        "evidence": "I had always wanted to bat like Sunil Gavaskar and Viv Richards, who were my heroes."
    },
    {
        "page": 2,
        "question": "Why did Sachin change his school to Shardashram Vidyamandir?",
        "aliases": [
            "why did sachin change school",
            "why sachin changed to shardashram",
            "shardashram vidyamandir school",
            "why did sachin join shardashram"
        ],
        "direct_answer": "Shardashram gave immense importance to cricket, and Achrekar Sir was the cricket coach there.",
        "completed_sentence": "Sachin changed his school to Shardashram Vidyamandir because **[Achrekar Sir was the cricket coach there and the school gave great importance to cricket]**.",
        "explanation": "His previous school (New English School, Bandra) lacked cricket coaching, so Achrekar Sir advised him to switch to Shardashram to focus on cricket.",
        "evidence": "Achrekar Sir was the cricket coach at Shardashram Vidyamandir and the school gave a lot of importance to cricket."
    },
    {
        "page": 3,
        "question": "What did Sachin do during the thirty-minute break?",
        "aliases": [
            "what did sachin do during the break",
            "thirty minute break sachin",
            "vadapav sachin",
            "what did achrekar sir give him during break"
        ],
        "direct_answer": "He ate a vadapav bought with money given by Achrekar Sir.",
        "completed_sentence": "During the thirty-minute break, Achrekar Sir would give Sachin money to buy a **[vadapav]**.",
        "explanation": "According to the textbook, between morning and afternoon practice sessions, Achrekar Sir gave Sachin money for a quick snack.",
        "evidence": "In between, Sir would give me some money to go and have a vadapav (a popular Mumbai snack)."
    },
    {
        "page": 3,
        "question": "What was placed on top of the stumps in the last 15 minutes?",
        "aliases": [
            "what was placed on top of stumps",
            "one rupee coin stumps",
            "stumps coin sachin",
            "last 15 minutes of session sachin",
            "how many one rupee coins did sachin win"
        ],
        "direct_answer": "A one-rupee coin",
        "completed_sentence": "In the last 15 minutes of practice, Achrekar Sir would place a **[one-rupee coin]** on top of the stumps.",
        "explanation": "According to the book, every bowler in the camp bowled at Sachin; if he survived without getting out, he won the coin. Sachin earned 13 such coins.",
        "evidence": "For the last fifteen minutes, Sir would place a one-rupee coin on top of the stumps. If I managed not to get out, the coin was mine."
    },
    {
        "page": 4,
        "question": "Who is Sachin Tendulkar?",
        "aliases": [
            "who is sachin tendulkar",
            "about sachin tendulkar",
            "sachin tendulkar profile"
        ],
        "direct_answer": "One of the greatest Indian cricketers and the first sportsperson to receive the Bharat Ratna.",
        "completed_sentence": "Sachin Tendulkar is **[a legendary Indian cricketer who scored 100 international centuries and received the Bharat Ratna]**.",
        "explanation": "Born on 24 April 1973 in Mumbai, he represented India for 24 years, scoring over 34,000 international runs.",
        "evidence": "Sachin Ramesh Tendulkar is an Indian former international cricketer widely regarded as one of the greatest batsmen in the history of cricket."
    },
    {
        "page": 6,
        "question": "'Achrekar was a sincere coach'. Substantiate.",
        "aliases": [
            "achrekar was a sincere coach",
            "substantiate achrekar was a sincere coach",
            "achrekar sincerity",
            "how was achrekar a sincere coach",
            "character sketch of achrekar"
        ],
        "direct_answer": "Achrekar Sir was a sincere, devoted mentor who instilled discipline, endurance, and dedication in Sachin.",
        "completed_sentence": "Achrekar proved his sincerity by **[conducting rigorous training from 7:30 AM to 7:00 PM, correcting Sachin's mistakes with strict discipline, and constantly pushing him to excel]**.",
        "explanation": "According to the textbook:\n\n1. Rigorous Training: Sir spent entire days coaching at Shivaji Park from dawn to dusk.\n2. Strict Discipline & Tough Love: When Sachin skipped practice to watch an inter-school match, Sir reprimanded him, saying: 'Don't play for others to watch; make others watch you play.'\n3. Innovative Incentives: Placing the one-rupee coin on the stumps trained Sachin to bat through extreme fatigue.",
        "evidence": "Sir was a strict disciplinarian and did everything he could for me. I owe myself to him."
    },
    {
        "page": 6,
        "question": "Match the words in column A with their synonym in column B (Unit 1)",
        "aliases": [
            "match column a with column b unit 1",
            "unit 1 synonyms match",
            "synonyms match unit 1",
            "match synonyms learning the game"
        ],
        "direct_answer": "Unit 1 Synonyms Matched",
        "completed_sentence": "ease ➔ **[effortlessly]**, emulate ➔ **[imitate]**, overawed ➔ **[impressed]**, inducted ➔ **[admitted]**.",
        "matches": [
            [
                "ease",
                "effortlessly"
            ],
            [
                "emulate",
                "imitate"
            ],
            [
                "overawed",
                "impressed"
            ],
            [
                "inducted",
                "admitted"
            ]
        ],
        "explanation": "Vocabulary exercise from Unit 1: Learning the Game.",
        "evidence": "Page 6 Exercise A: Match the words in column A with their synonym in column B."
    },
    {
        "page": 6,
        "question": "Match the words in column A with their antonym in column B (Unit 1)",
        "aliases": [
            "unit 1 antonyms match",
            "antonyms match unit 1",
            "match antonyms learning the game"
        ],
        "direct_answer": "Unit 1 Antonyms Matched",
        "completed_sentence": "concentrate ➔ **[distract]**, inevitable ➔ **[preventable]**, survive ➔ **[perish]**, immense ➔ **[tiny]**.",
        "matches": [
            [
                "concentrate",
                "distract"
            ],
            [
                "inevitable",
                "preventable"
            ],
            [
                "survive",
                "perish"
            ],
            [
                "immense",
                "tiny"
            ]
        ],
        "explanation": "Antonym matching exercise from Unit 1.",
        "evidence": "Page 6 Exercise B: Match the words in column A with their antonym in column B."
    },
    {
        "page": 20,
        "question": "Who was Shiro in The Envious Neighbour?",
        "aliases": [
            "who was shiro",
            "shiro dog",
            "dog in the envious neighbour"
        ],
        "direct_answer": "Shiro was the faithful pet dog of the kind old couple.",
        "completed_sentence": "Shiro was **[the faithful pet dog of the kind old couple]** who led them to a buried treasure of gold and silver.",
        "explanation": "According to the story, the kind couple treated Shiro like their own child and shared their food with him.",
        "evidence": "The old couple had a pet dog called Shiro, whom they loved as if he were their own baby."
    },
    {
        "page": 25,
        "question": "The old farmer and his wife loved the dog",
        "aliases": [
            "the old farmer and his wife loved the dog",
            "old farmer loved dog",
            "the old farmer and his wife loved the dog because"
        ],
        "options": [
            {
                "letter": "a",
                "text": "because it helped them in their day-to-day work."
            },
            {
                "letter": "b",
                "text": "as if it was their own baby."
            },
            {
                "letter": "c",
                "text": "as they were kind to all living beings."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) as if it was their own baby.",
        "completed_sentence": "The old farmer and his wife loved the dog **[as if it was their own baby]** (Option b).",
        "explanation": "According to the textbook folktale, the kind couple had no children and treated Shiro with great affection, feeding him tidbits from their own feast.",
        "evidence": "Book Page 25 Exercise B.1: The old farmer and his wife loved the dog b) as if it was their own baby."
    },
    {
        "page": 25,
        "question": "When the old couple became rich, they",
        "aliases": [
            "when the old couple became rich they",
            "when old couple became rich",
            "old couple became rich they"
        ],
        "options": [
            {
                "letter": "a",
                "text": "gave the dog better food."
            },
            {
                "letter": "b",
                "text": "invited their greedy neighbours to a feast."
            },
            {
                "letter": "c",
                "text": "lived a comfortable life and were generous towards their poor neighbours."
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) lived a comfortable life and were generous towards their poor neighbours.",
        "completed_sentence": "When the old couple became rich, they **[lived a comfortable life and were generous towards their poor neighbours]** (Option c).",
        "explanation": "According to the text, the good old couple bought rice-fields and corn-fields, gave alms to the poor, and shared their wealth.",
        "evidence": "Book Page 25 Exercise B.2: When the old couple became rich, they c) lived a comfortable life and were generous towards their poor neighbours."
    },
    {
        "page": 26,
        "question": "The greedy couple borrowed the mortar to make",
        "aliases": [
            "the greedy couple borrowed the mortar to make",
            "greedy couple borrowed mortar",
            "why greedy couple borrowed mortar"
        ],
        "options": [
            {
                "letter": "a",
                "text": "rich pastry and bean sauce."
            },
            {
                "letter": "b",
                "text": "magic ash to win rewards."
            },
            {
                "letter": "c",
                "text": "a pile of gold."
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) a pile of gold.",
        "completed_sentence": "The greedy couple borrowed the mortar to make **[a pile of gold]** (Option c).",
        "explanation": "Having seen the good couple pound rice into sparkling gold grains, the covetous neighbours borrowed the mortar expecting to get rich.",
        "evidence": "Book Page 26 Exercise B.3: The greedy couple borrowed the mortar to make c) a pile of gold."
    },
    {
        "page": 28,
        "question": "Who was the visitor?",
        "aliases": [
            "who was the visitor",
            "who is the visitor",
            "who was the man in i cant climb trees anymore",
            "the visitor ruskin bond",
            "who came to the house"
        ],
        "direct_answer": "A middle-aged man revisiting his childhood house in Dehradun.",
        "completed_sentence": "The visitor was **[a middle-aged man who returned to revisit the old house where he lived with his grandfather twenty-five years ago]**.",
        "explanation": "According to Ruskin Bond's story, the visitor returns not to purchase the property, but to seek the nostalgia and spirit of his youth.",
        "evidence": "He stood on the grass verge by the side of the road and looked over the garden wall at the old house. It had not changed much."
    },
    {
        "page": 28,
        "question": "The old house was built with _________.",
        "aliases": [
            "the old house was built with",
            "old house built with",
            "house granite i cant climb trees"
        ],
        "direct_answer": "solid blocks of granite",
        "completed_sentence": "The old house was built with **[solid blocks of granite]**.",
        "explanation": "The house was sturdy and built with granite blocks; only a new outhouse was added.",
        "evidence": "The old house built with solid blocks of granite wasn't altered at all."
    },
    {
        "page": 29,
        "question": "Who was the little girl in the house?",
        "aliases": [
            "who was the little girl",
            "little girl ruskin bond",
            "girl in the house",
            "girl with ribbon"
        ],
        "direct_answer": "A twelve-year-old girl with lively dark eyes whose father had recently purchased the house.",
        "completed_sentence": "The girl in the garden was **[a twelve-year-old lively girl with dark eyes]** whose family was now living in the house.",
        "explanation": "Her father was an army colonel who bought the bungalow.",
        "evidence": "A girl of about twelve, with lively dark eyes and a hair ribbon, came walking down the pathway."
    },
    {
        "page": 30,
        "question": "What did the visitor hide in the jackfruit tree?",
        "aliases": [
            "what did the visitor hide in the jackfruit tree",
            "what did the visitor hide in the tree",
            "iron cross jackfruit tree",
            "what was in the jackfruit tree",
            "what did the man leave in the tree"
        ],
        "direct_answer": "An Iron Cross (a military medal)",
        "completed_sentence": "The visitor hid an **[Iron Cross]** (a German military medal given to his grandfather during the First World War) in a hollow in the jackfruit tree.",
        "explanation": "According to the story, he kept his boyhood treasures in the tree hollow and forgot to take the Iron Cross when moving away.",
        "evidence": "‘I left it in the jackfruit tree.’ ‘What was it?’ ‘An Iron Cross. It was given to my grandfather by a British king.’"
    },
    {
        "page": 32,
        "question": "The story I Can't Climb Trees Anymore highlights the importance of ________",
        "aliases": [
            "the story i cant climb trees anymore highlights the importance of",
            "highlights the importance of",
            "i cant climb trees anymore highlights"
        ],
        "options": [
            {
                "letter": "a",
                "text": "old age."
            },
            {
                "letter": "b",
                "text": "youth."
            },
            {
                "letter": "c",
                "text": "adulthood."
            },
            {
                "letter": "d",
                "text": "middle age."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) youth.",
        "completed_sentence": "The story 'I Can't Climb Trees Anymore' highlights the importance of **[youth]** (Option b).",
        "explanation": "The central theme reflects on the magic, joy, and carefree innocence of youth, which remains in our memories even when age takes away our physical agility.",
        "evidence": "Book Page 32 Exercise B.1: The story I Can’t Climb Trees Anymore highlights the importance of b) youth."
    },
    {
        "page": 32,
        "question": "The house which was visited by the man____________",
        "aliases": [
            "the house which was visited by the man",
            "house visited by the man",
            "house which was visited"
        ],
        "options": [
            {
                "letter": "a",
                "text": "remained unchanged."
            },
            {
                "letter": "b",
                "text": "was totally changed."
            },
            {
                "letter": "c",
                "text": "was slightly repaired."
            },
            {
                "letter": "d",
                "text": "was given a facelift."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) remained unchanged.",
        "completed_sentence": "The house which was visited by the man **[remained unchanged]** (Option a).",
        "explanation": "Built with solid granite blocks, the main house was unaltered twenty-five years later, except for a newly built outhouse.",
        "evidence": "Book Page 32 Exercise B.2: The house which was visited by the man a) remained unchanged."
    },
    {
        "page": 33,
        "question": "Who said, 'A blessing rests on the house where the shadow of a tree falls'?",
        "aliases": [
            "a blessing rests on the house where the shadow of a tree falls",
            "who said a blessing rests on the house",
            "shadow of a tree falls who said"
        ],
        "options": [
            {
                "letter": "a",
                "text": "Grand mother"
            },
            {
                "letter": "b",
                "text": "Uncle"
            },
            {
                "letter": "c",
                "text": "Grand father"
            },
            {
                "letter": "d",
                "text": "The visitor"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) Grand mother.",
        "completed_sentence": "'A blessing rests on the house where the shadow of a tree falls' was said by the **[Grand mother]** (Option a).",
        "explanation": "The visitor fondly remembers his grandmother quoting this proverb to explain why she loved the towering trees around the house.",
        "evidence": "Book Page 33 Exercise B.3: a) Grand mother."
    },
    {
        "page": 33,
        "question": "The visitor came back to the house because he ________________",
        "aliases": [
            "the visitor came back to the house because he",
            "visitor came back because",
            "why visitor came back options"
        ],
        "options": [
            {
                "letter": "a",
                "text": "wanted to see the jackfruit tree."
            },
            {
                "letter": "b",
                "text": "was looking for his lost youth."
            },
            {
                "letter": "c",
                "text": "wanted to look again at his old house."
            },
            {
                "letter": "d",
                "text": "wanted to buy the house."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) was looking for his lost youth.",
        "completed_sentence": "The visitor came back to the house because he **[was looking for his lost youth]** (Option b).",
        "explanation": "He explicitly tells the girl that he didn't come for the Iron Cross or to buy the house, but to reconnect with the spirit of his youth.",
        "evidence": "Book Page 33 Exercise B.4: The visitor came back to the house because he b) was looking for his lost youth."
    },
    {
        "page": 33,
        "question": "The visitor gifted the _________ to the little girl.",
        "aliases": [
            "the visitor gifted the to the little girl",
            "visitor gifted the to girl",
            "visitor gift to girl",
            "what did the visitor gift the little girl",
            "the visitor gifted the"
        ],
        "options": [
            {
                "letter": "a",
                "text": "iron cross"
            },
            {
                "letter": "b",
                "text": "marbles"
            },
            {
                "letter": "c",
                "text": "bronze medal"
            },
            {
                "letter": "d",
                "text": "old coins"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) iron cross.",
        "completed_sentence": "The visitor gifted the **[iron cross]** to the little girl (Option a).",
        "explanation": "When the girl retrieved the grandfather's Iron Cross from the hollow trunk of the jackfruit tree, he asked her to keep it.",
        "evidence": "Book Page 33 Exercise B.5: The visitor gifted the a) iron cross to the little girl."
    },
    {
        "page": 33,
        "question": "Why couldn't the visitor climb the tree anymore?",
        "aliases": [
            "why couldnt the visitor climb the tree anymore",
            "why visitor cant climb trees",
            "why did he not climb the tree"
        ],
        "direct_answer": "He had grown older and no longer had the physical agility of a young boy.",
        "completed_sentence": "The visitor could not climb the tree anymore because **[he had grown older, lost his agility, and realized his boyhood days had passed]**.",
        "explanation": "He sat on the garden wall instead, understanding that physical youth cannot be regained, though its memory endures.",
        "evidence": "‘I can't climb trees anymore,’ he smiled. ‘I used to climb to the top branch, but not now.’"
    },
    {
        "page": 33,
        "question": "Match the words in column A with the meanings in column B (Unit 2)",
        "aliases": [
            "match column a with meanings in column b unit 2",
            "unit 2 vocabulary match",
            "match meanings unit 2",
            "pruning chiming drenched unit 2"
        ],
        "direct_answer": "Unit 2 Vocabulary Matched",
        "completed_sentence": "pruning ➔ **[trimming a plant]**, chiming ➔ **[ringing music]**, drenched ➔ **[soaked with water]**, dizzy ➔ **[feeling unstable]**.",
        "matches": [
            [
                "pruning",
                "trimming a plant"
            ],
            [
                "chiming",
                "ringing music"
            ],
            [
                "drenched",
                "soaked with water"
            ],
            [
                "dizzy",
                "feeling unstable"
            ]
        ],
        "explanation": "Vocabulary match exercise from Unit 2: I Can't Climb Trees Anymore.",
        "evidence": "Page 33 Exercise B: Match the words in column A with their meanings in column B."
    },
    {
        "page": 45,
        "question": "What kind of book did Tommy find in The Fun They Had?",
        "aliases": [
            "what did tommy find",
            "tommy found a real book",
            "the fun they had book",
            "margie tommy book"
        ],
        "direct_answer": "A real, old printed book made of paper with crinkly yellow pages.",
        "completed_sentence": "Tommy found a **[real printed book made of paper with yellow, crinkly pages]** in the attic.",
        "explanation": "In 2157, books were only electronic telebooks on screens, so a paper book was strange to Margie and Tommy.",
        "evidence": "Today Tommy found a real book! It was a very old book. Margie’s grandfather once said that when he was a little boy his grandfather told him that there was a time when all stories were printed on paper."
    },
    {
        "page": 46,
        "question": "Who was the County Inspector in The Fun They Had?",
        "aliases": [
            "who was the county inspector",
            "county inspector fun they had",
            "who repaired margies teacher"
        ],
        "direct_answer": "A round little man with a red face and a box of tools who repaired mechanical teachers.",
        "completed_sentence": "The County Inspector was **[a round little man with a red face]** who slowed down Margie's geography sector to a normal ten-year-old level.",
        "explanation": "Margie's mother called him because Margie was doing badly in geography tests.",
        "evidence": "He was a round little man with a red face and a whole box of tools with dials and wires."
    },
    {
        "page": 53,
        "question": "Explain the river in Old Man River",
        "aliases": [
            "explain the river",
            "what happened to the river in old man river",
            "river old man river",
            "the river was rising",
            "flood in old man river"
        ],
        "direct_answer": "The river had risen dangerously after a heavy cloudburst, causing the dam to break and flooding the town.",
        "completed_sentence": "The river rose rapidly due to **[a severe cloudburst and the breaking of the town dam]**, cutting off power and marooning the children.",
        "explanation": "In Dorothy Deming's play, the rising river floods the yard up to the porch, submerges bridges, and forces Amy, Rose, Betty, and Sara onto the roof for safety.",
        "evidence": "Jim: 'The water is up around the garage! The Thompson bridge is washed out and the dam gave way! The river is rising fast!'"
    },
    {
        "page": 60,
        "question": "There was no power because_______",
        "aliases": [
            "there was no power because",
            "why was there no power",
            "power house old man river",
            "why there was no electricity old man river"
        ],
        "options": [
            {
                "letter": "a",
                "text": "the power house was out of commission."
            },
            {
                "letter": "b",
                "text": "the power house was flooded."
            },
            {
                "letter": "c",
                "text": "the dam gave away."
            },
            {
                "letter": "d",
                "text": "there was fire."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) the power house was out of commission.",
        "completed_sentence": "There was no power because **[the power house was out of commission]** (Option a).",
        "explanation": "According to the play, flood waters disabled the electrical generators, forcing the children to use candles, flashlights, and lanterns.",
        "evidence": "Book Page 60 Exercise A.4: There was no power because a. the power house was out of commission."
    },
    {
        "page": 60,
        "question": "Why did they splint up Sara's leg with pillows?",
        "aliases": [
            "why did they splint up saras leg with pillows",
            "splint up saras leg with pillows",
            "saras leg pillows",
            "sara broken leg"
        ],
        "options": [
            {
                "letter": "a",
                "text": "She was unconscious out of fear."
            },
            {
                "letter": "b",
                "text": "She had broken her leg below the knee."
            },
            {
                "letter": "c",
                "text": "She was too lazy to walk."
            },
            {
                "letter": "d",
                "text": "She was making a fuss."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) She had broken her leg below the knee.",
        "completed_sentence": "They splinted up Sara's leg with pillows because **[she had broken her leg below the knee]** (Option b).",
        "explanation": "Sara fell off the step ladder in the attic. Jim and Amy immobilized the fractured leg using pillows and umbrellas until the Red Cross nurse arrived.",
        "evidence": "Book Page 60 Exercise A.5: Why did they splint up Sara's leg with pillows? b. She had broken her leg below the knee."
    },
    {
        "page": 58,
        "question": "How did the Red Cross help the children in Old Man River?",
        "aliases": [
            "how did red cross help",
            "red cross old man river",
            "mr peters miss marsh",
            "rescue in old man river"
        ],
        "direct_answer": "They arrived in a rescue boat with a nurse, splinted Sara's leg, and brought lanterns, coffee, and safe shelter.",
        "completed_sentence": "The Red Cross helped by **[sending a rescue boat with Mr. Peters and Miss Marsh to evacuate Sara on a stretcher and provide food and supplies]**.",
        "explanation": "Amy thanked Mr. Peters, who replied: 'Don't thank me, thank the Red Cross!'",
        "evidence": "Mr. Peters: 'Don't thank me, thank the Red Cross. We will get Sara safely to the emergency hospital at the high school.'"
    },
    {
        "page": 86,
        "question": "Brij started a tea shop because he wanted to",
        "aliases": [
            "brij started a tea shop because he wanted to",
            "why brij started a tea shop",
            "brij tea shop wanted to"
        ],
        "options": [
            {
                "letter": "a",
                "text": "start a company."
            },
            {
                "letter": "b",
                "text": "serve the people."
            },
            {
                "letter": "c",
                "text": "go on a pilgrimage."
            },
            {
                "letter": "d",
                "text": "become a tour guide."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) serve the people.",
        "completed_sentence": "Brij started a tea shop because he wanted to **[serve the people]** (Option b).",
        "explanation": "Grateful for the Army officer who saved his sister Bhuli, Brij found joy and peace in offering hot tea to tired travellers without taking money.",
        "evidence": "Book Page 86 Exercise B.1: Brij started a tea shop because he wanted to b) serve the people."
    },
    {
        "page": 86,
        "question": "Molthi was completely devastated because of",
        "aliases": [
            "molthi was completely devastated because of",
            "molthi devastated because of",
            "why molthi was devastated"
        ],
        "options": [
            {
                "letter": "a",
                "text": "a high intensity earthquake."
            },
            {
                "letter": "b",
                "text": "thunder and hail storm."
            },
            {
                "letter": "c",
                "text": "drought and famine."
            },
            {
                "letter": "d",
                "text": "flash floods."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) a high intensity earthquake.",
        "completed_sentence": "Molthi was completely devastated because of **[a high intensity earthquake]** (Option a).",
        "explanation": "The epicentre destroyed 602 out of 670 villages in the Garhwal valley within five minutes, flattening all stone houses in Molthi.",
        "evidence": "Book Page 86 Exercise B.2: Molthi was completely devastated because of a) a high intensity earthquake."
    },
    {
        "page": 86,
        "question": "The brother searched everywhere and looked dejected because",
        "aliases": [
            "the brother searched everywhere and looked dejected because",
            "brother looked dejected because",
            "brij looked dejected because"
        ],
        "options": [
            {
                "letter": "a",
                "text": "he couldn't find his house."
            },
            {
                "letter": "b",
                "text": "he couldn't locate his sister."
            },
            {
                "letter": "c",
                "text": "he was hungry and didn’t eat for a few days."
            },
            {
                "letter": "d",
                "text": "he lost his school books."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) he couldn't locate his sister.",
        "completed_sentence": "The brother searched everywhere and looked dejected because **[he couldn't locate his sister]** (Option b).",
        "explanation": "His two-year-old sister Bhuli was missing among the ruins. Brij wept on his knees searching through the stones until soldiers rescued her.",
        "evidence": "Book Page 86 Exercise B.3: The brother searched everywhere and looked dejected because b) he couldn't locate his sister."
    },
    {
        "page": 86,
        "question": "The boy had great reverence and respect for Army officers as they",
        "aliases": [
            "the boy had great reverence and respect for army officers as they",
            "reverence for army officers",
            "brij respect for army officers"
        ],
        "options": [
            {
                "letter": "a",
                "text": "were brave and courageous."
            },
            {
                "letter": "b",
                "text": "worked day and night."
            },
            {
                "letter": "c",
                "text": "saved his sister from death."
            },
            {
                "letter": "d",
                "text": "all the above."
            }
        ],
        "correct_option": "d",
        "direct_answer": "Option d) all the above.",
        "completed_sentence": "The boy had great reverence and respect for Army officers as they **[all the above]** (Option d).",
        "explanation": "The Army officer and his soldiers laboured doggedly through the night under petromax lamps to unearth Bhuli alive after 116 hours.",
        "evidence": "Book Page 86 Exercise B.4: The boy had great reverence and respect for Army officers as they d) all the above."
    },
    {
        "page": 86,
        "question": "Brij finally offered the traveller a",
        "aliases": [
            "brij finally offered the traveller a",
            "brij offered the traveller a",
            "what did brij offer the traveller"
        ],
        "options": [
            {
                "letter": "a",
                "text": "cup of milk"
            },
            {
                "letter": "b",
                "text": "cup of tea"
            },
            {
                "letter": "c",
                "text": "glass of water"
            },
            {
                "letter": "d",
                "text": "cup of coffee"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) cup of tea.",
        "completed_sentence": "Brij finally offered the traveller a **[cup of tea]** (Option b).",
        "explanation": "Brij served him hot tea and refused payment, saying: 'No, no money... you were tired. All I offered you was a cup of tea.'",
        "evidence": "Book Page 86 Exercise B.5: Brij finally offered the traveller a b) cup of tea."
    },
    {
        "page": 88,
        "question": "What did he steal in Seventeen Oranges?",
        "aliases": [
            "what did he steal",
            "what did the narrator steal",
            "what did he steal in seventeen oranges",
            "what was stolen in seventeen oranges",
            "narrator stole what"
        ],
        "direct_answer": "Seventeen big oranges from the docks.",
        "completed_sentence": "The narrator was caught because he stole **[seventeen oranges]** from a crate at the London docks and hid them in his pockets.",
        "explanation": "He worked for the Swift Delivery Company, loved eating oranges, and stuffed 17 of them into his pockets and apron.",
        "evidence": "A policeman found seventeen oranges hidden away in my pockets. He locked me up and I have never eaten an orange since."
    },
    {
        "page": 88,
        "question": "Where did the narrator work in Seventeen Oranges?",
        "aliases": [
            "where did the narrator work in seventeen oranges",
            "narrator work seventeen oranges",
            "swift delivery company",
            "docks seventeen oranges"
        ],
        "direct_answer": "Swift Delivery Company at the London docks.",
        "completed_sentence": "The narrator worked as a cart driver for the **[Swift Delivery Company]** at the docks.",
        "explanation": "He drove a pony and cart, delivering parcels to and from ships.",
        "evidence": "I used to drive a little pony-and-cart for the Swift Delivery Company, and I often went in and out of the docks."
    },
    {
        "page": 89,
        "question": "What was Clem Jones carrying in the box?",
        "aliases": [
            "what was clem jones carrying in the box",
            "clem jones box",
            "clem jones cat",
            "clem jones cheese",
            "what was inside clem jones box"
        ],
        "direct_answer": "First a ship's cat, which leaped out, and then a large Dutch cheese!",
        "completed_sentence": "When Clem Jones was forced to open his box, a **[ship's cat jumped out into the docks]**, but when he came back, the box concealed **[a large Dutch cheese]**.",
        "explanation": "Clem cleverly staged the cat's escape so Pongo wouldn't inspect the box closely the second time.",
        "evidence": "Out jumped a ship's cat. Clem ran after the cat. Two minutes later, Clem came back with the same box tightly shut... In the box, there was a large Dutch cheese!"
    },
    {
        "page": 90,
        "question": "Who was Pongo in Seventeen Oranges?",
        "aliases": [
            "who was pongo",
            "pongo policeman",
            "who caught the narrator in seventeen oranges"
        ],
        "direct_answer": "A strict and suspicious policeman on duty at the dock gates.",
        "completed_sentence": "Pongo was **[a dock policeman who caught the narrator with seventeen stolen oranges]**.",
        "explanation": "Pongo locked the narrator in his cabin while he went to fetch another officer as a witness.",
        "evidence": "Pongo the policeman caught me by the collar, looked into my pockets, and found seventeen big oranges."
    },
    {
        "page": 91,
        "question": "What did the narrator do with the seventeen oranges?",
        "aliases": [
            "what did the narrator do with the seventeen oranges",
            "how narrator destroyed evidence",
            "did he eat the seventeen oranges",
            "swallow pips peel"
        ],
        "direct_answer": "He swallowed every single orange, including the seeds (pips) and peels, to destroy all evidence.",
        "completed_sentence": "The narrator **[ate and swallowed all seventeen oranges, pips, and peels]** so there was no evidence left when Pongo returned.",
        "explanation": "The voice in his head urged him: 'Swallow it! You have to swallow all the evidence!'",
        "evidence": "‘You have to swallow the pips too,’ said the voice in my head. ‘You have to swallow all the evidence.’ I swallowed them all."
    },
    {
        "page": 93,
        "question": "The narrator was very fond of ________________",
        "aliases": [
            "the narrator was very fond of",
            "narrator fond of",
            "fond of seventeen oranges"
        ],
        "options": [
            {
                "letter": "a",
                "text": "reading detective stories."
            },
            {
                "letter": "b",
                "text": "driving a pony-and-cart."
            },
            {
                "letter": "c",
                "text": "eating oranges."
            },
            {
                "letter": "d",
                "text": "munching away at something."
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) eating oranges.",
        "completed_sentence": "The narrator was very fond of **[eating oranges]** (Option c).",
        "explanation": "He loved oranges so much he used to eat them all day and every day at the docks.",
        "evidence": "Book Page 93 Exercise A.1: The narrator was very fond of c) eating oranges."
    },
    {
        "page": 93,
        "question": "The narrator was searched by the policeman, because __________",
        "aliases": [
            "the narrator was searched by the policeman because",
            "why narrator was searched",
            "policeman searched narrator"
        ],
        "options": [
            {
                "letter": "a",
                "text": "the oranges could be smelt."
            },
            {
                "letter": "b",
                "text": "he was singing songs."
            },
            {
                "letter": "c",
                "text": "he was carrying a box."
            },
            {
                "letter": "d",
                "text": "his pockets were bulging."
            }
        ],
        "correct_option": "d",
        "direct_answer": "Option d) his pockets were bulging.",
        "completed_sentence": "The narrator was searched by the policeman, because **[his pockets were bulging]** (Option d).",
        "explanation": "Pongo noticed the boy's pockets and apron bulging with the shape of seventeen large oranges.",
        "evidence": "Book Page 93 Exercise A.2: The narrator was searched by the policeman, because d) his pockets were bulging."
    },
    {
        "page": 93,
        "question": "The narrator kept his mouth shut when questioned by Pongo, because __________",
        "aliases": [
            "the narrator kept his mouth shut when questioned by pongo because",
            "why narrator kept mouth shut",
            "kept mouth shut pongo"
        ],
        "options": [
            {
                "letter": "a",
                "text": "anything said would be held as evidence against him."
            },
            {
                "letter": "b",
                "text": "the oranges would fall out."
            },
            {
                "letter": "c",
                "text": "he did not steal the oranges."
            },
            {
                "letter": "d",
                "text": "he was scared of Pongo."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) anything said would be held as evidence against him.",
        "completed_sentence": "The narrator kept his mouth shut when questioned by Pongo, because **[anything said would be held as evidence against him]** (Option a).",
        "explanation": "He knew legal procedures from detective stories and chose not to incriminate himself.",
        "evidence": "Book Page 93 Exercise A.3: The narrator kept his mouth shut when questioned by Pongo, because a) anything said would be held as evidence against him."
    },
    {
        "page": 93,
        "question": "The voice in the narrator’s head advised him to____________",
        "aliases": [
            "the voice in the narrators head advised him to",
            "voice in head seventeen oranges",
            "voice advised him"
        ],
        "options": [
            {
                "letter": "a",
                "text": "confess the truth to Pongo."
            },
            {
                "letter": "b",
                "text": "eat all the oranges."
            },
            {
                "letter": "c",
                "text": "deny his guilt."
            },
            {
                "letter": "d",
                "text": "hide all the oranges."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) eat all the oranges.",
        "completed_sentence": "The voice in the narrator's head advised him to **[eat all the oranges]** (Option b).",
        "explanation": "Destroying the physical evidence (eating all 17 oranges including pips and peels) was the only way to escape prosecution.",
        "evidence": "Book Page 93 Exercise A.4: The voice in the narrator’s head advised him to b) eat all the oranges."
    },
    {
        "page": 93,
        "question": "Pongo found no trace of the oranges on the table, because ______",
        "aliases": [
            "pongo found no trace of the oranges on the table because",
            "no trace of oranges because",
            "why pongo found no oranges"
        ],
        "options": [
            {
                "letter": "a",
                "text": "Pongo’s mate had stolen them."
            },
            {
                "letter": "b",
                "text": "all the oranges were sold."
            },
            {
                "letter": "c",
                "text": "the narrator had eaten them all."
            },
            {
                "letter": "d",
                "text": "they disappeared mysteriously."
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) the narrator had eaten them all.",
        "completed_sentence": "Pongo found no trace of the oranges on the table, because **[the narrator had eaten them all]** (Option c).",
        "explanation": "Pongo searched everywhere, but the evidence was already in the boy's stomach.",
        "evidence": "Book Page 93 Exercise A.5: Pongo found no trace of the oranges on the table, because c) the narrator had eaten them all."
    },
    {
        "page": 97,
        "question": "Match the phrasal verbs in Column A with their meanings in Column B (Unit 4)",
        "aliases": [
            "match phrasal verbs unit 4",
            "phrasal verbs column a column b unit 4",
            "match phrasal verbs seventeen oranges"
        ],
        "direct_answer": "Unit 4 Phrasal Verbs Matched",
        "completed_sentence": "catch on ➔ **[become popular]**, clear out ➔ **[leave quickly]**, run into ➔ **[meet by chance]**, look into ➔ **[investigate]**.",
        "matches": [
            [
                "catch on",
                "become popular"
            ],
            [
                "clear out",
                "leave quickly"
            ],
            [
                "run into",
                "meet by chance"
            ],
            [
                "look into",
                "investigate"
            ]
        ],
        "explanation": "Phrasal verbs matching exercise from Unit 4: Seventeen Oranges.",
        "evidence": "Page 97 Exercise A: Match the phrasal verbs in Column A with their meanings in Column B."
    },
    {
        "page": 102,
        "question": "What is the theme of the poem The Spider and the Fly?",
        "aliases": [
            "theme of the spider and the fly",
            "moral of the spider and the fly",
            "what lesson does spider and fly teach",
            "message of the spider and the fly"
        ],
        "direct_answer": "Never succumb to vanity, false flattery, and deceptive invitations.",
        "completed_sentence": "The poem teaches readers **[never to heed the flattering words of cunning evil-doers and predators]**.",
        "explanation": "The spider exploits the fly's vanity about her brilliant eyes and gauzy wings to trap and devour her.",
        "evidence": "And now dear little children, who may this story read, To idle, silly flattering words, I pray you ne'er give heed."
    },
    {
        "page": 105,
        "question": "Write a character sketch of the spider",
        "aliases": [
            "write a character sketch of the spider",
            "character sketch of the spider",
            "sketch of spider",
            "describe the spider in the spider and the fly",
            "character traits of spider"
        ],
        "direct_answer": "A cunning, flattering predator who lures the innocent fly into his web through deceit and vanity.",
        "completed_sentence": "The spider is **[a cunning, manipulative predator who uses deceit and excessive flattery to trap his prey]**.",
        "explanation": "According to the poem 'The Spider and the Fly' by Mary Botham Howitt:\n\n1. Deceitful & Sly: He pretends to offer hospitality, inviting the fly to his 'prettiest little parlour' and offering soft resting beds.\n2. Master of Flattery: When practical bribes fail, he attacks the fly's vanity, praising her 'gauzy wings', 'brilliant eyes', and 'robes of pearl and silver'.\n3. Patient & Ruthless: He knows flattery never fails. The moment the fly returns, he pounces, drags her into his dismal den, and devours her.\n4. Moral Warning: Represents sweet-tongued predators in society who exploit human vanity.",
        "evidence": "Book Page 102-105: 'Sweet creature!' said the Spider, 'you’re witty and you’re wise, How handsome are your gauzy wings, how brilliant are your eyes!'"
    },
    {
        "page": 105,
        "question": "Write a character sketch of the fly",
        "aliases": [
            "write a character sketch of the fly",
            "character sketch of the fly",
            "describe the fly",
            "traits of the fly"
        ],
        "direct_answer": "Initially cautious and sensible, but ultimately blinded by vanity and false flattery.",
        "completed_sentence": "The fly is **[initially cautious and sensible, but ultimately blinded by vanity and false flattery]**.",
        "explanation": "According to the poem:\n\n1. Sensible Caution: She initially rejects all invitations, knowing that whoever enters the spider's parlour never comes down again.\n2. Fatal Flaw (Vanity): She cannot resist compliments about her diamond eyes and beautiful crest.\n3. Gullibility: Trusting sweet words instead of past wisdom leads to her tragic downfall.",
        "evidence": "Book Page 102-105: 'Oh no, no,' said the little Fly, 'to ask me is in vain, For who goes up your winding stair can ne'er come down again.'"
    },
    {
        "page": 106,
        "question": "Without trust there is no ______________.",
        "aliases": [
            "without trust there is no",
            "without trust there is no blank",
            "trust listening passage",
            "without trust there is no _____"
        ],
        "direct_answer": "relationship at all",
        "completed_sentence": "Without trust there is no **[relationship at all]**.",
        "explanation": "Listening passage from Unit 4 on the value of trust and integrity in human relationships.",
        "evidence": "Book Page 106 / Page 207 (Unit 4 Listening Passage): 'Without trust there is no relationship at all.'"
    },
    {
        "page": 106,
        "question": "______________ is a very rare thing to find in life.",
        "aliases": [
            "is a very rare thing to find in life",
            "rare thing to find in life",
            "blank is a very rare thing"
        ],
        "direct_answer": "Trust",
        "completed_sentence": "**[Trust]** is a very rare thing to find in life.",
        "explanation": "Listening passage from Unit 4: Trust is precious, rare, and takes years to build.",
        "evidence": "Book Page 106 / Page 207: 'Trust is a very rare thing to find in life.'"
    },
    {
        "page": 106,
        "question": "When people betray you learn from the _____________.",
        "aliases": [
            "when people betray you learn from the",
            "learn from the situation trust",
            "betray you learn from"
        ],
        "direct_answer": "situation",
        "completed_sentence": "When people betray you learn from the **[situation]**.",
        "explanation": "Listening passage from Unit 4: Betrayal offers a lesson in discernment rather than bitterness.",
        "evidence": "Book Page 106 / Page 207: 'When people betray you learn from the situation.'"
    },
    {
        "page": 106,
        "question": "Don't let small bumps on the road _____________.",
        "aliases": [
            "dont let small bumps on the road",
            "small bumps on the road",
            "bumps on the road trust"
        ],
        "direct_answer": "throw you back",
        "completed_sentence": "Don't let small bumps on the road **[throw you back]**.",
        "explanation": "Listening passage from Unit 4: Resilience allows us to move forward despite setbacks.",
        "evidence": "Book Page 106 / Page 207: 'Don't let small bumps on the road throw you back.'"
    },
    {
        "page": 106,
        "question": "If we keep moving forward you will have a wonderfully __________________.",
        "aliases": [
            "if we keep moving forward you will have a wonderfully",
            "wonderfully fulfilling life",
            "moving forward wonderfully"
        ],
        "direct_answer": "fulfilling life",
        "completed_sentence": "If we keep moving forward you will have a wonderfully **[fulfilling life]**.",
        "explanation": "Listening passage from Unit 4: Perseverance and moving forward lead to personal fulfillment.",
        "evidence": "Book Page 106 / Page 207: 'If we keep moving forward you will have a wonderfully fulfilling life.'"
    },
    {
        "page": 107,
        "question": "If you are asked to give a happy ending to the poem, how will you save the fly?",
        "aliases": [
            "give a happy ending to the poem",
            "how will you save the fly",
            "happy ending spider and fly",
            "save the fly happy ending"
        ],
        "direct_answer": "The fly heeds her instincts, remembers her mother's advice, and flies away to safety.",
        "completed_sentence": "In an alternative happy ending, **[the fly spots the sticky web in time, recalls her mother's warning against vanity, and buzzes safely out the open window]**.",
        "explanation": "According to the story:\n\n1. Alertness: The fly suddenly notices the severed wings of past victims in the web.\n2. Wisdom Over Vanity: She thanks the spider politely for the compliment but refuses to step near the winding stair.\n3. Triumph: She zooms into the sunlight, spreading the message to other insects to beware of flattering predators.",
        "evidence": "Page 107 Exercise: 'If you are asked to give a happy ending to the poem, how will you save the fly?'"
    },
    {
        "page": 110,
        "question": "What was the cat doing?",
        "aliases": [
            "what was the cat doing",
            "what did the cat do",
            "cat somersaults",
            "peter the cat doing",
            "how did the cat react to pain killer",
            "cat jumping around room"
        ],
        "direct_answer": "Peter the cat sprang into the air, did wild somersaults around the room, and leaped out through the window!",
        "completed_sentence": "After drinking the pain-killer, Peter the cat **[sprang two yards into the air, did frantic somersaults, banged into flowerpots, and sailed through the open window]**.",
        "explanation": "According to the textbook, Tom Sawyer fed Aunt Polly's pain-killer to Peter the cat, which triggered an explosive burst of crazy energy in the cat.",
        "evidence": "Peter sprang two yards into the air, yelled frantic war-whoops, went tearing around the house doing somersaults, and leaped out through the open window."
    },
    {
        "page": 110,
        "question": "Who was Peter in The Cat and the Pain-Killer?",
        "aliases": [
            "who was peter",
            "peter the cat",
            "what was the name of aunt polly's cat",
            "name of the cat"
        ],
        "direct_answer": "Peter was Aunt Polly's yellow pet cat.",
        "completed_sentence": "Peter was **[Aunt Polly's pet cat]** whom Tom gave a dose of pain-killer with a teaspoon.",
        "explanation": "Peter purred and begged for a taste, not knowing the scorching taste of the medicine.",
        "evidence": "Peter, his aunt's yellow cat, came purring along, eyeing the teaspoon greedily and begging for a taste."
    },
    {
        "page": 109,
        "question": "Why was Tom Sawyer sad and unhappy?",
        "aliases": [
            "why was tom sawyer sad",
            "why was tom unhappy",
            "why tom was depressed",
            "becky thatcher stopped coming"
        ],
        "direct_answer": "His schoolmate Becky Thatcher had fallen ill and stopped coming to school.",
        "completed_sentence": "Tom became depressed because **[Becky Thatcher, his friend, had stopped coming to school]**.",
        "explanation": "The charm of life was gone for Tom; he put away his bat and hoop and lost interest in playing.",
        "evidence": "Becky Thatcher, his friend, had stopped coming to school. This disturbed Tom. He became unhappy. The charm of life was gone."
    },
    {
        "page": 109,
        "question": "Who was Aunt Polly?",
        "aliases": [
            "who was aunt polly",
            "aunt polly character",
            "about aunt polly"
        ],
        "direct_answer": "Tom Sawyer's affectionate aunt who was obsessed with health remedies and quack medicines.",
        "completed_sentence": "Aunt Polly was **[Tom's loving but gullible aunt]** who tried various water treatments and pain-killers to cure Tom's depression.",
        "explanation": "She subscribed to health magazines and tested every new cure on Tom.",
        "evidence": "She was one of those people who are infatuated with patent medicines and all new-fangled methods of producing health."
    },
    {
        "page": 111,
        "question": "What did Aunt Polly do to Tom when she caught him giving medicine to the cat?",
        "aliases": [
            "what did aunt polly do to tom",
            "aunt polly cracked toms head",
            "aunt polly thimble"
        ],
        "direct_answer": "She lifted him by his ear and cracked his head soundly with her thimble.",
        "completed_sentence": "Aunt Polly **[raised Tom by his ear and cracked his head soundly with her thimble]** for tormenting the poor cat.",
        "explanation": "When Tom pointed out that Peter had no aunt to 'burn his bowels out' with medicine, Aunt Polly felt remorse and stopped dosing Tom.",
        "evidence": "Aunt Polly raised him by the usual handle – his ear – and cracked his head soundly with her thimble."
    },
    {
        "page": 117,
        "question": "What is the real elixir of life according to Sir C.V. Raman?",
        "aliases": [
            "what is the real elixir of life",
            "real elixir of life",
            "the real elixir of life according to sir cv raman is",
            "true elixir of life"
        ],
        "options": [
            {
                "letter": "a",
                "text": "divine Amrita."
            },
            {
                "letter": "b",
                "text": "plain, ordinary water."
            },
            {
                "letter": "c",
                "text": "fruit juice."
            },
            {
                "letter": "d",
                "text": "holy river water."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) plain, ordinary water.",
        "completed_sentence": "According to Sir C.V. Raman, the true elixir of life is **[plain, ordinary water]** (Option b).",
        "explanation": "While humanity searched for an imaginary divine nectar (Amrita), the real elixir of life is the commonest of all liquids: plain water.",
        "evidence": "Man has sought in vain for an imaginary elixir of life, the divine Amrita... But the true elixir of life lies near to our hands: it is the commonest of all liquids, plain water!"
    },
    {
        "page": 117,
        "question": "What is the imaginary elixir of life?",
        "aliases": [
            "what is the imaginary elixir of life",
            "imaginary elixir of life",
            "divine amrita"
        ],
        "direct_answer": "The divine Amrita (nectar thought to confer immortality).",
        "completed_sentence": "The imaginary elixir of life sought by humans is **[the divine Amrita]**.",
        "explanation": "Ancient mythology believed Amrita conferred immortality, but Raman argues ordinary water is far more wonderful.",
        "evidence": "Man has through the ages sought in vain for an imaginary elixir of life, the divine Amrita."
    },
    {
        "page": 118,
        "question": "Egypt was made by which river?",
        "aliases": [
            "egypt was made by which river",
            "which river made egypt",
            "egypt river nile",
            "river nile egypt"
        ],
        "options": [
            {
                "letter": "a",
                "text": "Amazon river."
            },
            {
                "letter": "b",
                "text": "River Nile."
            },
            {
                "letter": "c",
                "text": "River Ganges."
            },
            {
                "letter": "d",
                "text": "River Thames."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) River Nile.",
        "completed_sentence": "Egypt was made by the **[River Nile]** (Option b).",
        "explanation": "The life-giving waters and rich silt carried down from Abyssinia created the fertile Valley of the Nile amidst the desert.",
        "evidence": "Egypt, in fact, was made by its river. Its ancient civilization was created and is sustained by the life-giving waters of the Nile."
    },
    {
        "page": 118,
        "question": "Water in a landscape is compared to the _________ in a human face.",
        "aliases": [
            "water in a landscape is compared to",
            "water in landscape compared to",
            "compared to eyes in a human face",
            "eyes in a human face water"
        ],
        "options": [
            {
                "letter": "a",
                "text": "smile"
            },
            {
                "letter": "b",
                "text": "eyes"
            },
            {
                "letter": "c",
                "text": "tears"
            },
            {
                "letter": "d",
                "text": "beauty"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) eyes.",
        "completed_sentence": "Water in a landscape is compared to the **[eyes]** in a human face (Option b).",
        "explanation": "It reflects the mood of the hour, being bright and gay when the sun shines, and turning dark and gloomy when the sky is overcast.",
        "evidence": "Water in a landscape is compared to the eyes in a human face, reflecting the mood of the hour."
    },
    {
        "page": 119,
        "question": "What is the main cause of soil erosion?",
        "aliases": [
            "main cause of soil erosion",
            "what causes soil erosion",
            "soil erosion cv raman",
            "how is soil erosion caused"
        ],
        "direct_answer": "Sudden bursts of heavy rain leading to swift-flowing water washing away fertile topsoil.",
        "completed_sentence": "The main cause of soil erosion is **[sudden heavy bursts of rain causing swift-flowing water to wash away precious topsoil]**.",
        "explanation": "Slope of land, removal of protective vegetation, and lack of bunds accelerate erosion.",
        "evidence": "The flow of water can wash away the precious soil which is the foundation of all agriculture."
    },
    {
        "page": 119,
        "question": "How can soil erosion be prevented?",
        "aliases": [
            "how can soil erosion be prevented",
            "prevention of soil erosion",
            "measures to check soil erosion"
        ],
        "direct_answer": "Terracing of land, construction of bunds, contour cultivation, and planting trees (afforestation).",
        "completed_sentence": "Soil erosion can be prevented by **[terracing of land, building bunds, contour cultivation, and afforestation (planting trees)]**.",
        "explanation": "These measures check the velocity of rainwater run-off and conserve moisture.",
        "evidence": "Terracing of the land, the construction of bunds to check the flow of water, contour cultivation and the planting of appropriate vegetation are preventative measures."
    },
    {
        "page": 7,
        "question": "The Paralympic games are for _____",
        "aliases": [
            "the paralympic games are for",
            "paralympic games are for",
            "paralympics for who"
        ],
        "options": [
            {
                "letter": "a",
                "text": "children."
            },
            {
                "letter": "b",
                "text": "disabled people."
            },
            {
                "letter": "c",
                "text": "women."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) disabled people.",
        "completed_sentence": "The Paralympic games are for **[disabled people]** (Option b).",
        "explanation": "The Paralympics are a major international multi-sport event for athletes with disabilities.",
        "evidence": "Book Page 7 Exercise H.1: The Paralympic games are for b. disabled people."
    },
    {
        "page": 8,
        "question": "The Paralympic games usually happen ___________",
        "aliases": [
            "the paralympic games usually happen",
            "how often do paralympic games happen",
            "paralympics frequency"
        ],
        "options": [
            {
                "letter": "a",
                "text": "in Greece."
            },
            {
                "letter": "b",
                "text": "every four years."
            },
            {
                "letter": "c",
                "text": "after the Olympic Games."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) every four years.",
        "completed_sentence": "The Paralympic games usually happen **[every four years]** (Option b).",
        "explanation": "Like the Olympic Games, the Paralympic Games are held once every four years.",
        "evidence": "Book Page 8 Exercise H.2: The Paralympic games usually happen b. every four years."
    },
    {
        "page": 8,
        "question": "The first true Paralympic Games happened in Rome in _________",
        "aliases": [
            "the first true paralympic games happened in rome in",
            "first paralympic games rome year",
            "when did first paralympic games happen in rome"
        ],
        "options": [
            {
                "letter": "a",
                "text": "1960."
            },
            {
                "letter": "b",
                "text": "1952."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) 1960.",
        "completed_sentence": "The first true Paralympic Games happened in Rome in **[1960]** (Option a).",
        "explanation": "The 1960 Summer Paralympics held in Rome, Italy, were the first official Paralympic Games.",
        "evidence": "Book Page 8 Exercise H.3: The first true Paralympic Games happened in Rome in a. 1960."
    },
    {
        "page": 8,
        "question": "In 394 BCE, the ________ stopped the Greek Olympic Games, because they didn’t like them.",
        "aliases": [
            "in 394 bce the stopped the greek olympic games",
            "who stopped the greek olympic games in 394 bce",
            "394 bce olympic games stopped by"
        ],
        "options": [
            {
                "letter": "a",
                "text": "Romans"
            },
            {
                "letter": "b",
                "text": "Greeks"
            },
            {
                "letter": "c",
                "text": "British"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) Romans",
        "completed_sentence": "In 394 BCE, the **[Romans]** stopped the Greek Olympic Games (Option a).",
        "explanation": "Roman Emperor Theodosius I banned the ancient Olympic Games in 393/394 AD as part of the campaign to impose Christianity.",
        "evidence": "Book Page 8 Exercise H.4: In 394 BCE, the Romans stopped the Greek Olympic Games."
    },
    {
        "page": 8,
        "question": "____________ was a doctor at the Stoke Mandeville hospital in England.",
        "aliases": [
            "was a doctor at the stoke mandeville hospital in england",
            "doctor at stoke mandeville hospital",
            "who was a doctor at the stoke mandeville hospital",
            "sir ludwig guttmann"
        ],
        "options": [
            {
                "letter": "a",
                "text": "Pierre de Coubertin"
            },
            {
                "letter": "b",
                "text": "Sir Ludwig Guttmann"
            },
            {
                "letter": "c",
                "text": "Natalie du Toit"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) Sir Ludwig Guttmann",
        "completed_sentence": "**[Sir Ludwig Guttmann]** was a doctor at the Stoke Mandeville hospital in England (Option b).",
        "explanation": "Dr. Ludwig Guttmann founded the Stoke Mandeville Games for disabled war veterans, which evolved into the Paralympics.",
        "evidence": "Book Page 8 Exercise H.5: Sir Ludwig Guttmann was a doctor at the Stoke Mandeville hospital in England."
    },
    {
        "page": 48,
        "question": "The old book was found by ____________________________________",
        "aliases": [
            "the old book was found by",
            "who found the old book",
            "old book found by"
        ],
        "direct_answer": "Tommy (in the attic of his house)",
        "completed_sentence": "The old book was found by **[Tommy in the attic of his house]**.",
        "explanation": "Tommy discovered an old printed paper book describing schools of centuries ago.",
        "evidence": "Book Page 48 Exercise D.1: The old book was found by Tommy."
    },
    {
        "page": 48,
        "question": "Margie was surprised to see the old book because ___________________________",
        "aliases": [
            "margie was surprised to see the old book because",
            "why was margie surprised to see the old book"
        ],
        "direct_answer": "the words stood still instead of moving on a television screen as they were supposed to",
        "completed_sentence": "Margie was surprised to see the old book because **[the words stood still instead of moving on a screen]**.",
        "explanation": "Used to telebooks where text continually moves, she was amazed that words stayed printed in place when re-reading pages.",
        "evidence": "Book Page 48 Exercise D.2: Margie was surprised to see the old book because the words stood still."
    },
    {
        "page": 48,
        "question": "The mechanical teacher was giving Margie__________________________________",
        "aliases": [
            "the mechanical teacher was giving margie",
            "what was the mechanical teacher giving margie"
        ],
        "direct_answer": "test after test in geography",
        "completed_sentence": "The mechanical teacher was giving Margie **[test after test in geography, and she was doing worse and worse]**.",
        "explanation": "Margie hated school because the computerized teacher repeatedly gave difficult geography tests.",
        "evidence": "Book Page 48 Exercise D.3: The mechanical teacher was giving Margie test after test in geography."
    },
    {
        "page": 48,
        "question": "Margie had to study always at the same time every day, because her mother said little girls ____________________________________________________________",
        "aliases": [
            "margie had to study always at the same time every day",
            "her mother said little girls learn better",
            "why did margie study at regular hours"
        ],
        "direct_answer": "learned better if they learned at regular hours",
        "completed_sentence": "Margie had to study at regular hours because her mother said little girls **[learned better if they learned at regular hours]**.",
        "explanation": "Mrs. Jones insisted that routine and consistent study schedules produced superior academic results.",
        "evidence": "Book Page 48 Exercise D.4: ...because her mother said little girls learned better if they learned at regular hours."
    },
    {
        "page": 48,
        "question": "The geography sector in mechanical teacher was ____________________________",
        "aliases": [
            "the geography sector in mechanical teacher was",
            "geography sector mechanical teacher"
        ],
        "direct_answer": "geared a little too quick",
        "completed_sentence": "The geography sector in the mechanical teacher was **[geared a little too quick for an average ten-year-old]**.",
        "explanation": "The County Inspector inspected the machine and adjusted its pace down to a standard 10-year-old level.",
        "evidence": "Book Page 48 Exercise D.5: The geography sector in mechanical teacher was geared a little too quick."
    },
    {
        "page": 104,
        "question": "Can you guess what was in the pantry?",
        "aliases": [
            "can you guess what was in the pantry",
            "what was in the spiders pantry",
            "spiders pantry"
        ],
        "direct_answer": "Dead remains and corpses of insects trapped and eaten earlier by the spider.",
        "completed_sentence": "In the spider's pantry were **[the remains and carcasses of insects and flies he had previously killed and eaten]**.",
        "explanation": "The cunning spider pretended to offer 'all that's nice', but the fly wisely noted she had heard what was really stored there.",
        "evidence": "Book Page 104 Exercise A.b: 'I have within my pantry, good store of all that’s nice... I’ve heard what’s in your pantry, and I do not wish to see!'"
    },
    {
        "page": 105,
        "question": "Why was the spider sure that the fly would come back again?",
        "aliases": [
            "why was the spider sure that the fly would come back again",
            "why was spider sure fly would return",
            "why spider knew fly would come back"
        ],
        "direct_answer": "Because he knew the fly was vain and was deeply flattered by his compliments about her beauty.",
        "completed_sentence": "The spider was confident the fly would return because **[he knew her foolish vanity and pride would lure her back after hearing his flattering words]**.",
        "explanation": "Knowing the power of vanity, the spider immediately went to his den and set his dining table, confident she would return.",
        "evidence": "Book Page 103/105: 'The Spider turned him round about, and went into his den, For well he knew the silly Fly would soon come back again.'"
    },
    {
        "page": 105,
        "question": "What was 'she' thinking of?",
        "aliases": [
            "what was she thinking of in the spider and the fly",
            "what was she thinking of",
            "what was the fly thinking of"
        ],
        "direct_answer": "Her brilliant eyes, her green and purple robes, and her crested head.",
        "completed_sentence": "She was thinking only of **[her brilliant eyes, her green and purple hue, and her crested head]**.",
        "explanation": "Blinded by the spider's praise, the fly forgot all caution and hovered closer and closer to the web.",
        "evidence": "Book Page 103/105: 'Thinking only of her brilliant eyes, and green and purple hue — Thinking only of her crested head — poor foolish thing!'"
    },
    {
        "page": 105,
        "question": "What is the advice given to the readers?",
        "aliases": [
            "what is the advice given to the readers",
            "advice to readers spider and fly",
            "what advice does poet give"
        ],
        "direct_answer": "Never give heed to idle, silly flattering words, and close heart, ear, and eye to evil counsellors.",
        "completed_sentence": "The poet advises children to **[never pay attention to silly flattering words and to close heart, ear, and eye against deceitful advisers]**.",
        "explanation": "Mary Howitt concludes the poem with a direct moral lesson warning children against sweet-talking deceivers.",
        "evidence": "Book Page 103/105: 'Unto an evil counsellor, close heart and ear and eye, And take a lesson from this tale, of the Spider and the Fly.'"
    },
    {
        "page": 105,
        "question": "The poem begins with the spider's_________ of the fly.",
        "aliases": [
            "the poem begins with the spiders",
            "complete the summary of the spider and the fly",
            "summary of the spider and the fly blank",
            "the poem begins with the spiders of the fly"
        ],
        "direct_answer": "welcoming / invitation",
        "completed_sentence": "The poem begins with the spider's **[welcoming / invitation]** of the fly into his parlour.",
        "explanation": "Summary completion (Page 105): 1. welcoming 2. invites 3. prettiest 4. wise/alert 5. friend 6. bed 7. sheets 8. declines 9. flattery 10. wings 11. eyes 12. crest 13. looking-glass 14. flattered 15. prey 16. vanity.",
        "evidence": "Book Page 105 Exercise B: Complete the summary by filling in the spaces with suitable words."
    }
]

if __name__ == '__main__':
    with open('mobile_app/assets/qa_bank.json', 'w', encoding='utf-8') as f:
        json.dump(qa_list, f, indent=2, ensure_ascii=False)
    print(f"Total comprehensive Q&A items: {len(qa_list)}")
    print("Updated mobile_app/assets/qa_bank.json successfully!")
