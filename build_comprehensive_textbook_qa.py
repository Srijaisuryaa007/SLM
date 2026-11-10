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
    },
    {
        "page": 6,
        "question": "Match the words in column A with their synonym in column B",
        "aliases": [
            "match the words in column a with their synonym in column b",
            "synonyms match page 6",
            "match synonyms learning the game",
            "synonym match sachin",
            "synonyms column a and b page 6"
        ],
        "direct_answer": "1. ease ➔ effortless | 2. evolve ➔ progress | 3. excess ➔ surplus | 4. survive ➔ endure | 5. immense ➔ great",
        "matches": [
            [
                "1. ease",
                "effortless"
            ],
            [
                "2. evolve",
                "progress"
            ],
            [
                "3. excess",
                "surplus"
            ],
            [
                "4. survive",
                "endure"
            ],
            [
                "5. immense",
                "great"
            ]
        ],
        "completed_sentence": "Synonym Matches: **[ease ➔ effortless, evolve ➔ progress, excess ➔ surplus, survive ➔ endure, immense ➔ great]**.",
        "explanation": "Standard vocabulary synonym matching exercise from Unit 1: Learning the Game (Page 6).",
        "evidence": "Book Page 6 Vocabulary C: Match the words in column A with their synonym in column B."
    },
    {
        "page": 6,
        "question": "Match the words in column A with their antonym in column B",
        "aliases": [
            "match the words in column a with their antonym in column b",
            "antonyms match page 6",
            "match antonyms learning the game",
            "antonym match sachin",
            "antonyms column a and b page 6"
        ],
        "direct_answer": "1. concentrate ➔ distract | 2. inevitable ➔ preventable | 3. occasional ➔ continual | 4. complete ➔ incomplete | 5. insane ➔ wise / sane",
        "matches": [
            [
                "1. concentrate",
                "distract"
            ],
            [
                "2. inevitable",
                "preventable"
            ],
            [
                "3. occasional",
                "continual"
            ],
            [
                "4. complete",
                "incomplete"
            ],
            [
                "5. insane",
                "wise / sane"
            ]
        ],
        "completed_sentence": "Antonym Matches: **[concentrate ➔ distract, inevitable ➔ preventable, occasional ➔ continual, complete ➔ incomplete, insane ➔ wise]**.",
        "explanation": "Standard vocabulary antonym matching exercise from Unit 1: Learning the Game (Page 6).",
        "evidence": "Book Page 6 Vocabulary D: Match the words in column A with their antonym in column B."
    },
    {
        "page": 7,
        "question": "Consult a dictionary to find the homophones for the given words",
        "aliases": [
            "consult a dictionary to find the homophones for the given words",
            "homophones page 7",
            "find homophones page 7",
            "homophones dictionary exercise",
            "homophones learning the game"
        ],
        "direct_answer": "1. in ➔ inn | 2. know ➔ no | 3. be ➔ bee | 4. to ➔ two / too | 5. watt ➔ what | 6. right ➔ write | 7. were ➔ wear | 8. bare ➔ bear | 9. herd ➔ heard | 10. throne ➔ thrown",
        "matches": [
            [
                "1. in",
                "inn"
            ],
            [
                "2. know",
                "no"
            ],
            [
                "3. be",
                "bee"
            ],
            [
                "4. to",
                "two / too"
            ],
            [
                "5. watt",
                "what"
            ],
            [
                "6. right",
                "write / rite"
            ],
            [
                "7. were",
                "wear / ware"
            ],
            [
                "8. bare",
                "bear"
            ],
            [
                "9. herd",
                "heard"
            ],
            [
                "10. throne",
                "thrown"
            ]
        ],
        "completed_sentence": "Homophones: **[in ➔ inn, know ➔ no, be ➔ bee, to ➔ two, watt ➔ what, right ➔ write, were ➔ wear, bare ➔ bear, herd ➔ heard, throne ➔ thrown]**.",
        "explanation": "Homophones are words that sound identical in pronunciation but differ in meaning, origin, and spelling.",
        "evidence": "Book Page 7 Vocabulary F: Consult a dictionary, to find the homophones for the given words."
    },
    {
        "page": 25,
        "question": "Identify the character or speaker: They gathered the treasure.",
        "aliases": [
            "they gathered the treasure",
            "identify the character or speaker they gathered the treasure"
        ],
        "direct_answer": "The good old couple",
        "completed_sentence": "Character / Speaker: **[The good old couple]**.",
        "explanation": "After their faithful dog Muko guided them to a spot in the garden and barked, the kind couple dug and discovered gold and silver.",
        "evidence": "Book Page 25 Exercise A.1: 'They gathered the treasure.'"
    },
    {
        "page": 25,
        "question": "Identify the character or speaker: The pine tree under which I am buried, to be cut down and made into a mortar.",
        "aliases": [
            "the pine tree under which i am buried",
            "pine tree under which i am buried to be cut down and made into a mortar"
        ],
        "direct_answer": "The spirit of the dog (Muko)",
        "completed_sentence": "Character / Speaker: **[The spirit of the dog (Muko)]**.",
        "explanation": "The dog's spirit appeared in a dream to the good old man and instructed him to cut down the pine tree at his grave to make a mortar.",
        "evidence": "Book Page 25 Exercise A.2: 'The pine tree under which, I am burried, to be cut down and made into a mortar.'"
    },
    {
        "page": 25,
        "question": "Identify the character or speaker: They dug, and found nothing but a quantity of dirt and nasty offal.",
        "aliases": [
            "they dug and found nothing but a quantity of dirt and nasty offal",
            "found nothing but a quantity of dirt and nasty offal"
        ],
        "direct_answer": "The envious / greedy neighbours",
        "completed_sentence": "Character / Speaker: **[The envious / greedy neighbours]**.",
        "explanation": "Envious of the kind couple's fortune, the wicked neighbours borrowed the dog and forced him to dig, only finding putrid offal.",
        "evidence": "Book Page 25 Exercise A.3: 'They dug, and found nothing but a quantity of dirt and nasty offal.'"
    },
    {
        "page": 25,
        "question": "Identify the character or speaker: He had not to wait long before he was called into the prince's palace, and ordered to exhibit his power.",
        "aliases": [
            "he had not to wait long before he was called into the princes palace",
            "ordered to exhibit his power envious neighbour"
        ],
        "direct_answer": "The good old man",
        "completed_sentence": "Character / Speaker: **[The good old man]**.",
        "explanation": "The good old man used the magical ash from the burnt mortar to make withered cherry trees burst into blossom before the prince.",
        "evidence": "Book Page 25 Exercise A.4: 'He had not to wait long before he was called into the prince's palace, and ordered to exhibit his power.'"
    },
    {
        "page": 25,
        "question": "Identify the character or speaker: BOW, WOW, WOW!",
        "aliases": [
            "bow wow wow",
            "bow wow wow identify character or speaker"
        ],
        "direct_answer": "The dog (Muko)",
        "completed_sentence": "Character / Speaker: **[The dog (Muko)]**.",
        "explanation": "The faithful dog barked 'Bow, wow, wow!' while scratching the ground to alert his masters to the buried gold.",
        "evidence": "Book Page 25 Exercise A.5: 'BOW, WOW, WOW!'"
    },
    {
        "page": 32,
        "question": "Based on your understanding of the story, indicate True or False: I Can't Climb Trees Anymore",
        "aliases": [
            "true or false i cant climb trees anymore",
            "page 32 true or false",
            "indicate either t or f against the columns",
            "true false statements i cant climb trees anymore"
        ],
        "direct_answer": "1. F | 2. T | 3. T | 4. T | 5. T | 6. F | 7. T | 8. F | 9. F | 10. F",
        "matches": [
            [
                "1. The visitor had hidden a few old coins in the tree",
                "False (He hid an iron cross and marble)"
            ],
            [
                "2. The jackfruit tree was still there",
                "True"
            ],
            [
                "3. As a boy the visitor used to swing on the turnstile",
                "True"
            ],
            [
                "4. The visitor had sold the house",
                "True"
            ],
            [
                "5. A girl came out of the house",
                "True"
            ],
            [
                "6. The visitor’s grandfather used to sit on the stone bench",
                "False (Grandmother used to sit there)"
            ],
            [
                "7. The visitor was able to remember the music of a piano",
                "True"
            ],
            [
                "8. The visitor was able to climb the jackfruit tree",
                "False (He couldn't climb anymore)"
            ],
            [
                "9. The purpose of the visit was to buy the house back",
                "False (Looking for his lost youth)"
            ],
            [
                "10. The visitor climbed over the wall easily",
                "False (He struggled with breathing heavily)"
            ]
        ],
        "completed_sentence": "True/False Statements: **[1-F, 2-T, 3-T, 4-T, 5-T, 6-F, 7-T, 8-F, 9-F, 10-F]**.",
        "explanation": "True or False exercise from Unit 2: I Can't Climb Trees Anymore by Ruskin Bond (Page 32).",
        "evidence": "Book Page 32 Exercise A: Based on your understanding of the story, indicate either ‘T’ (True) or ‘F’ (False)."
    },
    {
        "page": 59,
        "question": "The radio announced that__________________________",
        "aliases": [
            "the radio announced that",
            "radio announced old man river",
            "what did the radio announce old man river"
        ],
        "options": [
            {
                "letter": "a",
                "text": "the river was above the flood stage."
            },
            {
                "letter": "b",
                "text": "the Burnet Dam had given way."
            },
            {
                "letter": "c",
                "text": "there will be a cloud burst."
            },
            {
                "letter": "d",
                "text": "they will be a cyclone."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) the river was above the flood stage.",
        "completed_sentence": "The radio announced that **[the river was above the flood stage]** (Option a).",
        "explanation": "In Dorothy Deming's play, the radio emergency broadcast announced rising water levels exceeding the flood stage.",
        "evidence": "Book Page 59 Exercise A.1: The radio announced that a. the river was above the flood stage."
    },
    {
        "page": 59,
        "question": "Mother couldn't get home from Mrs. Brant's because_____________",
        "aliases": [
            "mother couldnt get home from mrs brants because",
            "why couldnt mother get home old man river",
            "mother couldnt return because"
        ],
        "options": [
            {
                "letter": "a",
                "text": "it was raining heavily."
            },
            {
                "letter": "b",
                "text": "the bridges between home and the town were under water."
            },
            {
                "letter": "c",
                "text": "there was an emergency at Mrs. Brant's house."
            },
            {
                "letter": "d",
                "text": "she had broken her leg."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) the bridges between home and the town were under water.",
        "completed_sentence": "Mother couldn't get home because **[the bridges between home and the town were under water]** (Option b).",
        "explanation": "Flash flooding submerged the river bridges, stranding Mrs. March in town at Mrs. Brant's residence.",
        "evidence": "Book Page 59 Exercise A.2: Mother couldn't get home from Mrs. Brant's because b. the bridges between home and the town were under water."
    },
    {
        "page": 59,
        "question": "The Burnett Dam gave away as____________",
        "aliases": [
            "the burnett dam gave away as",
            "why did burnett dam give way",
            "burnett dam gave way because"
        ],
        "options": [
            {
                "letter": "a",
                "text": "it rained for days."
            },
            {
                "letter": "b",
                "text": "the dam was weak."
            },
            {
                "letter": "c",
                "text": "it rained heavily and the snow was melting."
            },
            {
                "letter": "d",
                "text": "the maintenance was poor."
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) it rained heavily and the snow was melting.",
        "completed_sentence": "The Burnett Dam gave away as **[it rained heavily and the snow was melting]** (Option c).",
        "explanation": "A violent cloudburst combined with rapid snowmelt overwhelmed the dam's capacity.",
        "evidence": "Book Page 59 Exercise A.3: The Burnett Dam gave away as c. it rained heavily and the snow was melting."
    },
    {
        "page": 60,
        "question": "Match the following by drawing a line across column A and B: Old Man River",
        "aliases": [
            "match the following old man river",
            "match the following by drawing a line across column a and b",
            "column a and b old man river",
            "match characters old man river",
            "amy betty rose sara match"
        ],
        "direct_answer": "1. Amy ➔ Blankets | 2. Betty ➔ Flashlight | 3. Rose ➔ Tubs and pails | 4. Sara ➔ Fractured leg | 5. Jim ➔ Rescues the children | 6. Penny Marsh ➔ Nurse | 7. Mr. Peters ➔ Red Cross | 8. Mother ➔ Mrs. Brant's | 9. Dick ➔ Dentist | 10. Dad ➔ To Chicago on business",
        "matches": [
            [
                "1. Amy",
                "Blankets"
            ],
            [
                "2. Betty",
                "Flashlight"
            ],
            [
                "3. Rose",
                "Tubs and pails"
            ],
            [
                "4. Sara",
                "Fractured leg"
            ],
            [
                "5. Jim",
                "Rescues the children"
            ],
            [
                "6. Penny Marsh",
                "Nurse"
            ],
            [
                "7. Mr. Peters",
                "Red Cross"
            ],
            [
                "8. Mother",
                "Mrs. Brant's"
            ],
            [
                "9. Dick",
                "Dentist"
            ],
            [
                "10. Dad",
                "To Chicago on business"
            ]
        ],
        "completed_sentence": "Old Man River Matches: **[Amy ➔ Blankets, Betty ➔ Flashlight, Rose ➔ Tubs & pails, Sara ➔ Fractured leg, Jim ➔ Rescues children, Penny Marsh ➔ Nurse, Mr. Peters ➔ Red Cross, Mother ➔ Mrs. Brant's, Dick ➔ Dentist, Dad ➔ Chicago]**.",
        "explanation": "Complete 10-character assignment matching table from the play Old Man River (Book Page 60).",
        "evidence": "Book Page 60 Exercise C: Match the following by drawing a line across column A and B."
    },
    {
        "page": 61,
        "question": "Using a dictionary, find out the synonyms and the antonyms of the words given below",
        "aliases": [
            "using a dictionary find out the synonyms and the antonyms of the words given below",
            "synonyms and antonyms page 61",
            "dictionary synonyms antonyms old man river",
            "hard flood interrupt scared synonyms antonyms",
            "vocabulary table page 61"
        ],
        "direct_answer": "1. Hard: Syn=difficult, Ant=easy | 2. Flood: Syn=deluge/overflow, Ant=drought/trickle | 3. Interrupt: Syn=disturb/break in, Ant=continue/proceed | 4. Scared: Syn=frightened, Ant=confident/bold | 5. Irritation: Syn=annoyance, Ant=delight/comfort | 6. Organize: Syn=arrange/plan, Ant=disorganize | 7. Serious: Syn=grave/critical, Ant=trivial/funny | 8. Snappy: Syn=irritable, Ant=patient/polite | 9. Emergency: Syn=crisis, Ant=normalcy | 10. Rescue: Syn=save/deliver, Ant=abandon/endanger",
        "matches": [
            [
                "1. Hard (Adj)",
                "Syn: difficult | Ant: easy"
            ],
            [
                "2. Flood (Noun/Verb)",
                "Syn: deluge, overflow | Ant: drought, trickle"
            ],
            [
                "3. Interrupt (Verb)",
                "Syn: disturb, break in | Ant: continue, proceed"
            ],
            [
                "4. Scared (Adj)",
                "Syn: frightened, terrified | Ant: confident, fearless"
            ],
            [
                "5. Irritation (Noun)",
                "Syn: annoyance | Ant: delight, pleasure"
            ],
            [
                "6. Organize (Verb)",
                "Syn: arrange, coordinate | Ant: confuse, disorganize"
            ],
            [
                "7. Serious (Adj)",
                "Syn: grave, solemn | Ant: trivial, lighthearted"
            ],
            [
                "8. Snappy (Adj)",
                "Syn: irritable, touchy | Ant: patient, calm"
            ],
            [
                "9. Emergency (Noun)",
                "Syn: crisis, urgency | Ant: calm, normalcy"
            ],
            [
                "10. Rescue (Verb/Noun)",
                "Syn: save, deliver | Ant: abandon, endanger"
            ]
        ],
        "completed_sentence": "Vocabulary Table: **[Hard (difficult/easy), Flood (deluge/drought), Interrupt (disturb/continue), Scared (frightened/confident), Irritation (annoyance/delight), Organize (arrange/confuse), Serious (grave/trivial), Snappy (irritable/patient), Emergency (crisis/normalcy), Rescue (save/abandon)]**.",
        "explanation": "Comprehensive dictionary exercise from Unit 3 (Page 61) defining parts of speech, synonyms, and antonyms for flood emergency terms.",
        "evidence": "Book Page 61 Vocabulary E: Using a dictionary, find out the synonyms and the antonyms of the words given below."
    },
    {
        "page": 94,
        "question": "The voice in his head asked the narrator to eat the evidence.",
        "aliases": [
            "the voice in his head asked the narrator to eat the evidence",
            "synonym of evidence seventeen oranges",
            "find the synonym for evidence"
        ],
        "options": [
            {
                "letter": "a",
                "text": "proof"
            },
            {
                "letter": "b",
                "text": "contradict"
            },
            {
                "letter": "c",
                "text": "disprove"
            },
            {
                "letter": "d",
                "text": "refute"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) proof",
        "completed_sentence": "The voice in his head asked the narrator to eat the **[proof]** (evidence) (Option a).",
        "explanation": "Evidence means available facts or information indicating whether a belief is valid; a synonym is proof.",
        "evidence": "Book Page 94 Exercise D.1: The voice in his head asked the narrator to eat the evidence. a) proof."
    },
    {
        "page": 94,
        "question": "Clem looked at Pongo furiously.",
        "aliases": [
            "clem looked at pongo furiously",
            "synonym of furiously seventeen oranges",
            "find the synonym for furiously"
        ],
        "options": [
            {
                "letter": "a",
                "text": "politely"
            },
            {
                "letter": "b",
                "text": "gently"
            },
            {
                "letter": "c",
                "text": "angrily"
            },
            {
                "letter": "d",
                "text": "calmly"
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) angrily",
        "completed_sentence": "Clem looked at Pongo **[angrily]** (furiously) (Option c).",
        "explanation": "Furiously means in an extremely angry or violent manner; a synonym is angrily.",
        "evidence": "Book Page 94 Exercise D.2: Clem looked at Pongo furiously. c) angrily."
    },
    {
        "page": 94,
        "question": "When Pongo caught the narrator with the oranges, he was very frightened.",
        "aliases": [
            "when pongo caught the narrator with the oranges he was very frightened",
            "synonym of frightened seventeen oranges",
            "find the synonym for frightened"
        ],
        "options": [
            {
                "letter": "a",
                "text": "undaunted"
            },
            {
                "letter": "b",
                "text": "afraid"
            },
            {
                "letter": "c",
                "text": "valiant"
            },
            {
                "letter": "d",
                "text": "brave"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) afraid",
        "completed_sentence": "When Pongo caught the narrator with the oranges, he was very **[afraid]** (frightened) (Option b).",
        "explanation": "Frightened means afraid or anxious; a direct synonym is afraid.",
        "evidence": "Book Page 94 Exercise D.3: When Pongo caught the narrator with the oranges, he was very frightened. b) afraid."
    },
    {
        "page": 94,
        "question": "The narrator was quiet, when Pongo questioned him.",
        "aliases": [
            "the narrator was quiet when pongo questioned him",
            "synonym of quiet seventeen oranges",
            "find the synonym for quiet"
        ],
        "options": [
            {
                "letter": "a",
                "text": "furious"
            },
            {
                "letter": "b",
                "text": "noisy"
            },
            {
                "letter": "c",
                "text": "silent"
            },
            {
                "letter": "d",
                "text": "agitated"
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) silent",
        "completed_sentence": "The narrator was **[silent]** (quiet), when Pongo questioned him (Option c).",
        "explanation": "Quiet in this context means keeping mouth shut and not speaking; a direct synonym is silent.",
        "evidence": "Book Page 94 Exercise D.4: The narrator was quiet, when Pongo questioned him. c) silent."
    },
    {
        "page": 94,
        "question": "The narrator was in trouble because he took the oranges.",
        "aliases": [
            "the narrator was in trouble because he took the oranges",
            "synonym of trouble seventeen oranges",
            "find the synonym for trouble"
        ],
        "options": [
            {
                "letter": "a",
                "text": "peace"
            },
            {
                "letter": "b",
                "text": "difficulty"
            },
            {
                "letter": "c",
                "text": "harmony"
            },
            {
                "letter": "d",
                "text": "comfort"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) difficulty",
        "completed_sentence": "The narrator was in **[difficulty]** (trouble) because he took the oranges (Option b).",
        "explanation": "Trouble denotes difficulty, distress, or problems; a direct synonym is difficulty.",
        "evidence": "Book Page 94 Exercise D.5: The narrator was in trouble because he took the oranges. b) difficulty."
    },
    {
        "page": 94,
        "question": "Seventeen oranges were hidden in the narrator’s pockets.",
        "aliases": [
            "seventeen oranges were hidden in the narrators pockets",
            "antonym of hidden seventeen oranges",
            "find the antonym for hidden"
        ],
        "options": [
            {
                "letter": "a",
                "text": "exposed"
            },
            {
                "letter": "b",
                "text": "masked"
            },
            {
                "letter": "c",
                "text": "concealed"
            },
            {
                "letter": "d",
                "text": "buried"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) exposed",
        "completed_sentence": "Seventeen oranges were **[exposed]** (antonym of hidden) in the pockets (Option a).",
        "explanation": "Hidden means kept out of sight; the antonym is exposed (visible, uncovered).",
        "evidence": "Book Page 94 Exercise E.1: Seventeen oranges were hidden in the narrator’s pockets. a) exposed."
    },
    {
        "page": 94,
        "question": "Clem Jones was ordered to open the box.",
        "aliases": [
            "clem jones was ordered to open the box",
            "antonym of ordered seventeen oranges",
            "find the antonym for ordered"
        ],
        "options": [
            {
                "letter": "a",
                "text": "prepared"
            },
            {
                "letter": "b",
                "text": "arranged"
            },
            {
                "letter": "c",
                "text": "forced"
            },
            {
                "letter": "d",
                "text": "requested"
            }
        ],
        "correct_option": "d",
        "direct_answer": "Option d) requested",
        "completed_sentence": "Clem Jones was **[requested]** (antonym of ordered) to open the box (Option d).",
        "explanation": "Ordered denotes commanding authoritatively; the opposite is requested (asking politely).",
        "evidence": "Book Page 94 Exercise E.2: Clem Jones was ordered to open the box. d) requested."
    },
    {
        "page": 94,
        "question": "Pongo locked the narrator inside the cabin.",
        "aliases": [
            "pongo locked the narrator inside the cabin",
            "antonym of locked seventeen oranges",
            "find the antonym for locked"
        ],
        "options": [
            {
                "letter": "a",
                "text": "closed"
            },
            {
                "letter": "b",
                "text": "sealed"
            },
            {
                "letter": "c",
                "text": "released"
            },
            {
                "letter": "d",
                "text": "chocked"
            }
        ],
        "correct_option": "c",
        "direct_answer": "Option c) released",
        "completed_sentence": "Pongo **[released]** (antonym of locked) the narrator inside the cabin (Option c).",
        "explanation": "Locked means fastened or confined; the opposite is released (set free).",
        "evidence": "Book Page 94 Exercise E.3: Pongo locked the narrator inside the cabin. c) released."
    },
    {
        "page": 94,
        "question": "Pongo carefully searched the narrator’s pockets.",
        "aliases": [
            "pongo carefully searched the narrators pockets",
            "antonym of carefully seventeen oranges",
            "find the antonym for carefully"
        ],
        "options": [
            {
                "letter": "a",
                "text": "attentively"
            },
            {
                "letter": "b",
                "text": "carelessly"
            },
            {
                "letter": "c",
                "text": "cautiously"
            },
            {
                "letter": "d",
                "text": "strictly"
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) carelessly",
        "completed_sentence": "Pongo **[carelessly]** (antonym of carefully) searched the pockets (Option b).",
        "explanation": "Carefully means with great attention; the antonym is carelessly.",
        "evidence": "Book Page 94 Exercise E.4: Pongo carefully searched the narrator’s pockets. b) carelessly."
    },
    {
        "page": 94,
        "question": "The narrator of the story felt very sick for a week",
        "aliases": [
            "the narrator of the story felt very sick for a week",
            "antonym of sick seventeen oranges",
            "find the antonym for sick"
        ],
        "options": [
            {
                "letter": "a",
                "text": "healthy"
            },
            {
                "letter": "b",
                "text": "disordered"
            },
            {
                "letter": "c",
                "text": "feeble"
            },
            {
                "letter": "d",
                "text": "unhealthy"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) healthy",
        "completed_sentence": "The narrator felt very **[healthy]** (antonym of sick) for a week (Option a).",
        "explanation": "Sick means unwell or ill; the antonym is healthy.",
        "evidence": "Book Page 94 Exercise E.5: The narrator of the story felt very sick for a week. a) healthy."
    },
    {
        "page": 96,
        "question": "In New York Mr Scotti left the plane because he thought he",
        "aliases": [
            "in new york mr scotti left the plane because he thought he",
            "mr scotti new york plane",
            "why did scotti get off plane in new york"
        ],
        "options": [
            {
                "letter": "a",
                "text": "had to change the plane."
            },
            {
                "letter": "b",
                "text": "was in Rome."
            },
            {
                "letter": "c",
                "text": "had to phone his cousins."
            },
            {
                "letter": "d",
                "text": "had to look at the airport."
            }
        ],
        "correct_option": "b",
        "direct_answer": "Option b) was in Rome.",
        "completed_sentence": "Mr Scotti left the plane because he thought he **[was in Rome]** (Option b).",
        "explanation": "On a flight from America to Italy, the plane made an interim stop at JFK Airport in New York. Scotti mistakenly believed he had reached Rome.",
        "evidence": "Book Page 96 Exercise K.1: In New York Mr Scotti left the plane because he thought he (b) was in Rome."
    },
    {
        "page": 96,
        "question": "He asked the policeman for information in Italian because he",
        "aliases": [
            "he asked the policeman for information in italian because he",
            "scotti policeman italian",
            "why scotti asked policeman in italian"
        ],
        "options": [
            {
                "letter": "a",
                "text": "thought he was in Italy."
            },
            {
                "letter": "b",
                "text": "knew the policeman."
            },
            {
                "letter": "c",
                "text": "didn't speak any other language."
            },
            {
                "letter": "d",
                "text": "liked the language."
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) thought he was in Italy.",
        "completed_sentence": "Scotti asked in Italian because he **[thought he was in Italy]** (Option a).",
        "explanation": "Convinced he was roaming the streets of Rome, he naturally addressed the officer in Italian.",
        "evidence": "Book Page 96 Exercise K.2: He asked the policeman for information in Italian because he (a) thought he was in Italy."
    },
    {
        "page": 96,
        "question": "On the next day, Mr Scotti was __________ at how the local people responded to his queries.",
        "aliases": [
            "on the next day mr scotti was at how the local people responded",
            "scotti surprised english drivers"
        ],
        "options": [
            {
                "letter": "a",
                "text": "surprised"
            },
            {
                "letter": "b",
                "text": "unhappy"
            },
            {
                "letter": "c",
                "text": "glad"
            },
            {
                "letter": "d",
                "text": "upset"
            }
        ],
        "correct_option": "a",
        "direct_answer": "Option a) surprised",
        "completed_sentence": "Mr Scotti was **[surprised]** at how the local people responded in English (Option a).",
        "explanation": "After travelling around by bus for 12 hours, he was baffled why everyone spoke English in what he thought was Rome.",
        "evidence": "Book Page 96 Exercise K.3: On the next day, Mr Scotti was (a) surprised."
    },
    {
        "page": 97,
        "question": "Find the meanings of phrasal verbs by using a dictionary",
        "aliases": [
            "find the meanings of phrasal verbs by using a dictionary",
            "phrasal verbs page 97",
            "phrasal verbs column a and b page 97",
            "meanings of phrasal verbs using dictionary seventeen oranges"
        ],
        "direct_answer": "1. fond of ➔ liking someone or something | 2. hidden away ➔ concealed in a secret place | 3. lock up ➔ to imprison or securely enclose | 4. laughed at ➔ ridiculed or mocked | 5. look at ➔ inspect or examine | 6. bring up ➔ raise or mention | 7. gave up ➔ surrendered or stopped trying | 8. went through ➔ examined thoroughly | 9. finish off ➔ consume or destroy completely | 10. figure out ➔ understand or solve",
        "matches": [
            [
                "1. fond of",
                "liking someone or something very much"
            ],
            [
                "2. hidden away",
                "concealed in a secret, secure place"
            ],
            [
                "3. lock up",
                "to imprison or shut in securely"
            ],
            [
                "4. laughed at",
                "ridiculed, teased, or mocked"
            ],
            [
                "5. look at",
                "to inspect, observe, or examine"
            ],
            [
                "6. bring up",
                "to raise, educate, or mention"
            ],
            [
                "7. gave up",
                "surrendered or stopped attempting"
            ],
            [
                "8. went through",
                "searched, examined, or experienced"
            ],
            [
                "9. finish off",
                "to consume, eat, or destroy completely"
            ],
            [
                "10. figure out",
                "to understand, solve, or calculate"
            ]
        ],
        "completed_sentence": "Phrasal Verbs Dictionary Meanings: **[fond of (liking), hidden away (concealed), lock up (imprison), laughed at (mocked), look at (inspect), bring up (mention), gave up (surrendered), went through (searched), finish off (consume completely), figure out (understand)]**.",
        "explanation": "Complete 10 phrasal verb dictionary definition exercise from Unit 4: Seventeen Oranges (Book Page 97).",
        "evidence": "Book Page 97 Grammar A: Find the meanings by using a dictionary and complete Column B."
    },
    {
        "page": 118,
        "question": "What is the 'wonderful difference' the writer talks about in the passage?",
        "aliases": [
            "what is the wonderful difference the writer talks about in the passage",
            "wonderful difference c v raman",
            "libyan desert and nile valley difference"
        ],
        "direct_answer": "The contrast between the arid Libyan desert and the green, fertile valley of the Nile.",
        "completed_sentence": "The wonderful difference is **[between the barren Libyan desert without a speck of green life, and the fertile, teeming valley of the River Nile]**.",
        "explanation": "Standing on the line separating the Libyan Desert from the Valley of the Nile, on one side is a sea of sand, while on the other is one of the most fertile areas on Earth, separated solely by the water of the Nile.",
        "evidence": "Book Page 118: 'On one side was visible a sea of billowing sand without a speck of green... on the other side lay one of the greenest, most fertile and densely populated areas... What made this wonderful difference? Why, it is the water of the River Nile!'"
    },
    {
        "page": 118,
        "question": "What is the 'cheering sight' mentioned in the paragraph?",
        "aliases": [
            "what is the cheering sight mentioned in the paragraph",
            "cheering sight water elixir",
            "rainfed tanks south india"
        ],
        "direct_answer": "The rainfed tanks of South India when they are full of water.",
        "completed_sentence": "The cheering sight is **[the rainfed tanks of South India when they are full of water]**.",
        "explanation": "Though often shallow, these South Indian tanks play a vital role in agriculture and are beautiful when reflecting the sunrise or sunset.",
        "evidence": "Book Page 118: 'The rainfed tanks that are so common in South India – Alas! often so sadly neglected in their maintenance – are a cheering sight when they are full.'"
    },
    {
        "page": 118,
        "question": "What does the writer compare water in a landscape to?",
        "aliases": [
            "what does the writer compare water in a landscape to",
            "water in landscape compared to",
            "eyes in a human face"
        ],
        "direct_answer": "The eyes in a human face, reflecting the mood of the hour.",
        "completed_sentence": "Water in a landscape is compared to **[the eyes in a human face, reflecting the mood of the hour]**.",
        "explanation": "It is bright and gay when the sun shines, and turns dark and gloomy when the sky is overcast.",
        "evidence": "Book Page 118: 'Water in a landscape may be compared to the eyes in a human face. It reflects the mood of the hour...'"
    },
    {
        "page": 119,
        "question": "How does the water in rainfed tanks get its colour?",
        "aliases": [
            "how does the water in rainfed tanks get its colour",
            "colour of water in rainfed tanks",
            "silt in suspension"
        ],
        "direct_answer": "From the silt or finely divided soil carried in suspension from the catchment area.",
        "completed_sentence": "Water in rainfed tanks gets its colour from **[the finely divided soil or silt carried in suspension, reflecting the nature of the earth in the catchment area]**.",
        "explanation": "The color varies with the earth in the catchment area and is most vivid immediately following rain.",
        "evidence": "Book Page 119: 'One of the most remarkable facts about water is its power to carry silt... This is the origin of the characteristic colour of the water in rainfed tanks.'"
    },
    {
        "page": 119,
        "question": "What other factors add to the erosion of precious soil?",
        "aliases": [
            "what other factors add to the erosion of precious soil",
            "contributory causes of soil erosion"
        ],
        "direct_answer": "The slope of the land, removal of vegetation, ruts gathering momentum, and absence of check bunds.",
        "completed_sentence": "Additional factors causing soil erosion are **[the slope of the land, removal of protective vegetative cover, ruts gathering flow momentum, and the absence of any checks to the water flow]**.",
        "explanation": "These factors accelerate the speed and volume of moving water, dislodging precious topsoil.",
        "evidence": "Book Page 119: 'Contributory causes are the slope of the land, removal of the natural protective coat of vegetation, the existence of ruts... and the absence of any checks of such flow.'"
    },
    {
        "page": 120,
        "question": "How does prevention of soil erosion serve a double purpose?",
        "aliases": [
            "how does prevention of soil erosion serve a double purpose",
            "double purpose soil erosion",
            "double purpose water conservation"
        ],
        "direct_answer": "It protects fertile topsoil from washing away, and conserves rainwater in the soil.",
        "completed_sentence": "Prevention of soil erosion serves a double purpose by **[preserving fertile topsoil from being washed away and keeping moisture stored in the ground where it is needed]**.",
        "explanation": "Techniques that check rushing water simultaneously conserve moisture in the ground, supporting crops.",
        "evidence": "Book Page 120: '...adoption of techniques preventing soil erosion would also help to conserve and keep the water where it is wanted... and such techniques therefore serve a double purpose.'"
    },
    {
        "page": 120,
        "question": "What are the two sources of water?",
        "aliases": [
            "what are the two sources of water",
            "two sources of water water elixir",
            "ultimate source of water"
        ],
        "direct_answer": "Rain (or snowfall) and artesian water.",
        "completed_sentence": "The two primary sources of water are **[rain/snowfall and artesian (sub-surface) water]**.",
        "explanation": "Rainfall is the ultimate primary source for all surface water, rivers, and seasonal agriculture.",
        "evidence": "Book Page 120: 'Apart from artesian water the ultimate source in all cases is rain or snowfall.'"
    },
    {
        "page": 120,
        "question": "What happens to the rain water?",
        "aliases": [
            "what happens to the rain water",
            "what happens to rainwater in india"
        ],
        "direct_answer": "An immense quantity runs off the ground into rivers and flows away to waste into the sea.",
        "completed_sentence": "An immense quantity of rain water **[runs off into streams and rivers and flows away into the sea as waste]**.",
        "explanation": "Harnessing these rivers on a national scale could turn scrub jungle into fertile farmland.",
        "evidence": "Book Page 120: 'Much of it flows down into the streams and rivers and ultimately finds its way to the sea. Incredibly large quantities of the precious fluid are thus lost to the country.'"
    },
    {
        "page": 121,
        "question": "What is the idea of civilized forest?",
        "aliases": [
            "what is the idea of civilized forest",
            "civilized forest c v raman",
            "afforestation civilized forest"
        ],
        "direct_answer": "Systematic planting of suitable trees in every available area as distinguished from wild, untamed jungle.",
        "completed_sentence": "A civilized forest is **[the systematic planting of suitable trees in every available area to create organized, productive forests as opposed to wild jungle]**.",
        "explanation": "Civilized forests check soil erosion, conserve rainfall, provide cheap firewood, and save farmyard manure for fertilization.",
        "evidence": "Book Page 121: 'The systematic planting of suitable trees in every possible or even in impossible areas, and the development of what one can call civilized forests, as distinguished from wild and untamed jungle, is one of the most urgent needs of India.'"
    },
    {
        "page": 121,
        "question": "What is the cheapest means of transport?",
        "aliases": [
            "what is the cheapest means of transport",
            "cheapest transport c v raman",
            "internal waterways transport"
        ],
        "direct_answer": "Boats and barges through canals and rivers (internal waterways).",
        "completed_sentence": "The cheapest means of internal transport is **[by boats and barges through canals and rivers (waterways)]**.",
        "explanation": "Water transport requires far less fuel and infrastructure expenditure than road or rail networks.",
        "evidence": "Book Page 121: 'By far the cheapest form of internal transport in a country is by boats and barges through canals and rivers.'"
    },
    {
        "page": 121,
        "question": "How can you make a difference in the countryside?",
        "aliases": [
            "how can you make a difference in the countryside",
            "difference in the countryside water elixir",
            "hydro electric power countryside"
        ],
        "direct_answer": "By developing internal waterways and tapping hydroelectric power from harnessed water.",
        "completed_sentence": "A difference in the countryside can be made by **[developing internal water transport and generating hydroelectric power to uplift the rural economy]**.",
        "explanation": "Electric power transforms agriculture, enables rural cottage industries, and improves village life.",
        "evidence": "Book Page 121: 'The availability of electric power would make a tremendous difference to the life of the countryside and enable rural economy to be improved in various directions.'"
    },
    {
        "page": 59,
        "question": "Based on your understanding of the play, choose the correct answer and fill in the blanks: Old Man River",
        "aliases": [
            "based on your understanding of the play choose the correct answer",
            "based on your understanding of the play choose the correct answer and fill in the blanks",
            "choose the correct answer old man river",
            "old man river mcqs"
        ],
        "direct_answer": "1. Option a) the river was above the flood stage | 2. Option b) bridges under water | 3. Option c) rained heavily and snow melting | 4. Option a) power house out of commission | 5. Option b) broken leg below knee",
        "matches": [
            [
                "1. The radio announced that",
                "Option a) the river was above the flood stage."
            ],
            [
                "2. Mother couldn't get home because",
                "Option b) the bridges between home and town were under water."
            ],
            [
                "3. The Burnett Dam gave away as",
                "Option c) it rained heavily and the snow was melting."
            ],
            [
                "4. There was no power because",
                "Option a) the power house was out of commission."
            ],
            [
                "5. Why splint up Sara's leg with pillows?",
                "Option b) She had broken her leg below the knee."
            ]
        ],
        "completed_sentence": "Old Man River (Page 59-60 MCQs): **[1-a, 2-b, 3-c, 4-a, 5-b]**.",
        "explanation": "Complete solutions to Section A: Choose the correct answer from the play Old Man River (Pages 59-60).",
        "evidence": "Book Page 59-60 Exercise A: Based on your understanding of the play, choose the correct answer and fill in the blanks."
    },
    {
        "page": 25,
        "question": "Based on your understanding of the story choose the right answers from the given options: The Envious Neighbour",
        "aliases": [
            "based on your understanding of the story choose the right answers from the given options",
            "choose the right answers the envious neighbour",
            "the envious neighbour mcqs"
        ],
        "direct_answer": "1. Option b) as if it was their own baby | 2. Option c) lived comfortable life and generous to poor | 3. Option c) a pile of gold",
        "matches": [
            [
                "1. The old farmer and his wife loved the dog",
                "Option b) as if it was their own baby."
            ],
            [
                "2. When the old couple became rich, they",
                "Option c) lived a comfortable life and were generous towards poor neighbours."
            ],
            [
                "3. The greedy couple borrowed the mortar to make",
                "Option c) a pile of gold."
            ]
        ],
        "completed_sentence": "The Envious Neighbour MCQs: **[1-b, 2-c, 3-c]**.",
        "explanation": "Complete solutions to Section B: Choose the right answers from The Envious Neighbour (Pages 25-26).",
        "evidence": "Book Page 25-26 Exercise B: Based on your understanding of the story choose the right answers."
    },
    {
        "page": 32,
        "question": "Based on your understanding of the story, answer the following questions by choosing the correct answer: I Can't Climb Trees Anymore",
        "aliases": [
            "based on your understanding of the story answer the following questions by choosing the correct answer",
            "choose the correct answer i cant climb trees anymore",
            "i cant climb trees anymore mcqs"
        ],
        "direct_answer": "1. Option b) youth | 2. Option a) remained unchanged | 3. Option a) Grand mother | 4. Option b) looking for lost youth | 5. Option a) iron cross",
        "matches": [
            [
                "1. The story highlights the importance of",
                "Option b) youth."
            ],
            [
                "2. The house visited by the man",
                "Option a) remained unchanged."
            ],
            [
                "3. Who said A blessing rests on the house where shadow falls?",
                "Option a) Grand mother."
            ],
            [
                "4. The visitor came back because he",
                "Option b) was looking for his lost youth."
            ],
            [
                "5. The visitor gifted to the little girl",
                "Option a) iron cross."
            ]
        ],
        "completed_sentence": "I Can't Climb Trees Anymore MCQs: **[1-b, 2-a, 3-a, 4-b, 5-a]**.",
        "explanation": "Complete solutions to Section B: Choose the correct answer from I Can't Climb Trees Anymore (Pages 32-33).",
        "evidence": "Book Page 32-33 Exercise B: Based on your understanding of the story, answer the following questions by choosing the correct answer."
    },
    {
        "page": 93,
        "question": "From your reading of the text, choose the correct answers: Seventeen Oranges",
        "aliases": [
            "from your reading of the text choose the correct answers",
            "choose the correct answers seventeen oranges",
            "seventeen oranges mcqs"
        ],
        "direct_answer": "1. Option c) eating oranges | 2. Option d) pockets were bulging | 3. Option a) anything said held as evidence | 4. Option b) eat all oranges | 5. Option c) narrator had eaten them all",
        "matches": [
            [
                "1. The narrator was very fond of",
                "Option c) eating oranges."
            ],
            [
                "2. Narrator searched by policeman because",
                "Option d) his pockets were bulging."
            ],
            [
                "3. Narrator kept mouth shut because",
                "Option a) anything said would be held as evidence."
            ],
            [
                "4. The voice in narrator's head advised him to",
                "Option b) eat all the oranges."
            ],
            [
                "5. Pongo found no trace of oranges because",
                "Option c) narrator had eaten them all."
            ]
        ],
        "completed_sentence": "Seventeen Oranges MCQs: **[1-c, 2-d, 3-a, 4-b, 5-c]**.",
        "explanation": "Complete solutions to Section A: Choose the correct answers from Seventeen Oranges (Page 93).",
        "evidence": "Book Page 93 Exercise A: From your reading of the text, choose the correct answers from the options given below."
    },
    {
        "page": 20,
        "question": "Complete the summary of the poem by filling in the blanks: Stopping by Woods on a Snowy Evening",
        "aliases": [
            "complete the summary of the poem by filling in the blanks",
            "stopping by woods summary",
            "after a long travel the poet entered",
            "summary of stopping by woods on a snowy evening",
            "after a long travel the poet entered a"
        ],
        "direct_answer": "1. wood | 2. belonged | 3. village | 4. see | 5. snow | 6. queer | 7. stopped without a farmhouse near | 8. frozen lake | 9. the darkest evening of the year | 10. mistake | 11. harness bells | 12. lovely, dark and deep | 13. promises to keep | 14. sleep / stay",
        "completed_sentence": "After a long travel the poet entered a **[wood]**. He wondered to whom the wood **[belonged]**! He realized that the owner lived in a **[village]**. He thought the owner would not be able to **[see]** him stopping to watch **[snow]** fill the woods. The horse felt it very **[queer]** to stop as he had never **[stopped without a farmhouse near]**. He was standing between the woods and **[frozen lake]**. The time was **[the darkest evening of the year]**. The horse indicated a **[mistake]** by shaking its **[harness bells]**. The woods are lovely, **[dark]** and **[deep]**. He realized he had worldly **[promises to keep]** which would not allow him to **[sleep]** for a long time.",
        "explanation": "Official complete textbook summary fill-in-the-blanks exercise from Unit 1: Stopping by Woods on a Snowy Evening (Page 20).",
        "evidence": "Book Page 20 Exercise C: Complete the summary of the poem by filling in the blanks."
    },
    {
        "page": 20,
        "question": "Why the poet has used the same line twice? And miles to go before I sleep",
        "aliases": [
            "why the poet has used the same line twice",
            "miles to go before i sleep repeated twice",
            "why is and miles to go before i sleep repeated"
        ],
        "direct_answer": "To emphasize the profound importance of fulfilling worldly duties and obligations before taking final rest (death).",
        "completed_sentence": "The poet repeats the line twice to **[strongly emphasize his heavy worldly duties and responsibilities before he can rest]**.",
        "explanation": "The repetition of 'And miles to go before I sleep' symbolizes both the literal journey remaining and the symbolic journey of life and responsibilities before death.",
        "evidence": "Book Page 20 Exercise 5.a: 'Why the poet has used the same line twice?'"
    },
    {
        "page": 20,
        "question": "Explain: miles to go before I sleep",
        "aliases": [
            "explain miles to go before i sleep",
            "meaning of miles to go before i sleep"
        ],
        "direct_answer": "It means the speaker has many promises, duties, and responsibilities to fulfill in life before he can rest or die.",
        "completed_sentence": "Miles to go before I sleep signifies **[the numerous commitments and responsibilities that must be fulfilled before eternal rest]**.",
        "explanation": "'Miles to go' represents life's unfinished journey and commitments, while 'sleep' represents rest or death.",
        "evidence": "Book Page 20 Exercise 5.b: 'Explain: miles to go before I sleep'"
    },
    {
        "page": 20,
        "question": "Identify the rhyme scheme used in each stanza: Stopping by Woods on a Snowy Evening",
        "aliases": [
            "identify the rhyme scheme used in each stanza",
            "rhyme scheme stopping by woods",
            "stopping by woods rhyme scheme stanza 1 2 3 4"
        ],
        "direct_answer": "Stanza 1: aaba | Stanza 2: bbcb | Stanza 3: ccdc | Stanza 4: dddd",
        "matches": [
            [
                "Stanza 1",
                "aaba (know, though, here, snow)"
            ],
            [
                "Stanza 2",
                "bbcb (queer, near, lake, year)"
            ],
            [
                "Stanza 3",
                "ccdc (shake, mistake, sweep, flake)"
            ],
            [
                "Stanza 4",
                "dddd (deep, keep, sleep, sleep)"
            ]
        ],
        "completed_sentence": "Rhyme Scheme: **[Stanza 1: aaba, Stanza 2: bbcb, Stanza 3: ccdc, Stanza 4: dddd]**.",
        "explanation": "Robert Frost employs interlocking chain rhyme (Rubaiyat stanza form), where the unrhymed third line sets the rhyme for the next stanza, concluding in dddd.",
        "evidence": "Book Page 20 Exercise E: Identify the rhyme scheme used in each stanza."
    },
    {
        "page": 20,
        "question": "What are the sounds heard by the poet? Stopping by Woods",
        "aliases": [
            "what are the sounds heard by the poet",
            "sounds heard in stopping by woods"
        ],
        "direct_answer": "The gentle shake of the horse's harness bells and the soft sweep of easy wind and downy snow flake.",
        "completed_sentence": "The sounds heard by the poet are **[the jingling of the harness bells and the gentle sweep of the easy wind and downy snow flake]**.",
        "explanation": "In stanza 3, Frost notes the quiet wilderness sounds: 'He gives his harness bells a shake... The only other sound's the sweep of easy wind and downy flake.'",
        "evidence": "Book Page 20 Exercise D.3: 'What are the sounds heard by the poet?'"
    },
    {
        "page": 20,
        "question": "What information does the poet highlight about the season and the time of the day in the poem? Stopping by Woods",
        "aliases": [
            "what information does the poet highlight about the season and the time of the day in the poem",
            "season and time of day stopping by woods"
        ],
        "direct_answer": "The season is winter (snow and frozen lake), and the time of day is the darkest evening of the year (winter solstice).",
        "completed_sentence": "The poet highlights that it is **[winter season (snow falling, frozen lake)]** during **[the darkest evening of the year]**.",
        "explanation": "Lines 'To watch his woods fill up with snow' and 'The darkest evening of the year' define the winter solstice setting.",
        "evidence": "Book Page 20 Exercise D.1: Season and time of day in Stopping by Woods."
    },
    {
        "page": 40,
        "question": "Complete the summary by filling in the given spaces with suitable words: A Poison Tree",
        "aliases": [
            "complete the summary by filling in the given spaces with suitable words",
            "a poison tree summary",
            "once the poet was angry with his friend he expressed his",
            "summary of a poison tree"
        ],
        "direct_answer": "(i) wrath | (ii) suppressed / concealed | (iii) sunned / deceived | (iv) tempted / enticed | (v) dead / outstretched",
        "completed_sentence": "Once the poet was angry with his friend. He expressed his (i) **[wrath]** and it ended. They became friendly but when he grew angry with his foe, he (ii) **[suppressed / concealed]** it and allowed his anger to grow. Day and night he watered it with his tears. He (iii) **[sunned / deceived]** his foe with false smiles and cunning tricks. The tree yielded a bright apple which (iv) **[tempted]** his foe to eat it stealthily. The next morning the poet was happy to see his foe lying (v) **[dead / outstretched]** under the tree.",
        "explanation": "Official complete textbook summary fill-in-the-blanks exercise from Unit 2: A Poison Tree (Page 40).",
        "evidence": "Book Page 40 Exercise B: Complete the summary by filling in the given spaces with suitable words."
    },
    {
        "page": 40,
        "question": "What does 'apple' signify in A Poison Tree?",
        "aliases": [
            "what does apple signify",
            "what does apple signify in a poison tree",
            "till it bore an apple bright what does apple signify"
        ],
        "direct_answer": "The apple signifies the tempting, visible, and fatal fruit of harboured anger, hatred, and deceit.",
        "completed_sentence": "The apple signifies **[the tempting and fatal outward result of suppressed wrath and malice]**.",
        "explanation": "Blake uses the bright apple as an allegory for hatred nurtured in secret until it bears deadly consequences.",
        "evidence": "Book Page 40 Exercise A.4.b: 'What does ‘apple’ signify?'"
    },
    {
        "page": 40,
        "question": "Why was the 'foe' found lying outstretched beneath the tree? A Poison Tree",
        "aliases": [
            "why was the foe found lying outstretched beneath the tree",
            "foe outstretched beneath the tree"
        ],
        "direct_answer": "The foe had secretly entered the garden at night, eaten the poisonous fruit of wrath, and died.",
        "completed_sentence": "The foe was lying outstretched because **[he had stolen into the garden at night, eaten the poison apple, and died]**.",
        "explanation": "In stanza 4, the foe saw the shining apple and stole into the garden when night veiled the pole, eating the fatal fruit.",
        "evidence": "Book Page 40 Exercise A.3.c: 'Why was the ‘foe’ found lying outstretched beneath the tree?'"
    },
    {
        "page": 40,
        "question": "What does 'it' refer to in 'And I watered it in fears'? A Poison Tree",
        "aliases": [
            "what does it refer to in and i watered it in fears",
            "and i watered it in fears what does it refer to"
        ],
        "direct_answer": "It refers to the poet's suppressed anger / wrath towards his foe.",
        "completed_sentence": "'It' refers to **[the poet's unexpressed anger and malice towards his enemy]**.",
        "explanation": "The poet personifies his suppressed wrath as a plant that he waters with fears and tears.",
        "evidence": "Book Page 40 Exercise A.2.a: 'What does ‘it’ refer to?'"
    },
    {
        "page": 41,
        "question": "What is the rhyme scheme of the stanza in A Poison Tree?",
        "aliases": [
            "what is the rhyme scheme of the stanza a poison tree",
            "rhyme scheme a poison tree"
        ],
        "direct_answer": "aabb (e.g. friend/end, foe/grow; fears/tears, smiles/wiles)",
        "completed_sentence": "The rhyme scheme is **[aabb]** throughout each four-line stanza.",
        "explanation": "William Blake constructs the poem using rhyming couplets: friend (a), end (a), foe (b), grow (b).",
        "evidence": "Book Page 41 Exercise E.1.ii: 'What is the rhyme scheme of the stanza?'"
    },
    {
        "page": 41,
        "question": "Identify the figure of speech in the title of the poem: A Poison Tree",
        "aliases": [
            "identify the figure of speech in the title of the poem a poison tree",
            "figure of speech title a poison tree"
        ],
        "direct_answer": "Metaphor (wrath and hatred are implicitly compared to a growing poisonous tree).",
        "completed_sentence": "The figure of speech is a **[Metaphor]**, comparing harboured anger to a deadly tree.",
        "explanation": "The title uses an extended metaphor where silent anger grows, blossoms, and produces fatal fruit.",
        "evidence": "Book Page 41 Exercise E.1.iii: 'Identify the figure of speech in the title of the poem.'"
    },
    {
        "page": 47,
        "question": "Identify the character or speaker: She was given test after test in geography.",
        "aliases": [
            "she was given test after test in geography",
            "identify character she was given test after test in geography"
        ],
        "direct_answer": "Margie",
        "completed_sentence": "Character / Speaker: **[Margie]**.",
        "explanation": "Margie was given continuous geography tests by her mechanical teacher, which had been geared too fast for her age.",
        "evidence": "Book Page 47 Exercise A.1: 'She was given test after test in geography.'"
    },
    {
        "page": 47,
        "question": "Identify the character or speaker: He was a round little man with a red face and a whole box of tools with dials and wires.",
        "aliases": [
            "he was a round little man with a red face",
            "round little man with a red face and a whole box of tools"
        ],
        "direct_answer": "The County Inspector",
        "completed_sentence": "Character / Speaker: **[The County Inspector]**.",
        "explanation": "The County Inspector was called by Margie's mother to inspect and fix Margie's malfunctioning mechanical teacher.",
        "evidence": "Book Page 47 Exercise A.2: 'He was a round little man with a red face and a whole box of tools with dials and wires.'"
    },
    {
        "page": 47,
        "question": "Identify the character or speaker: She had been hoping they would take the teacher away altogether.",
        "aliases": [
            "she had been hoping they would take the teacher away altogether",
            "hoping they would take the teacher away"
        ],
        "direct_answer": "Margie",
        "completed_sentence": "Character / Speaker: **[Margie]**.",
        "explanation": "Margie hoped the Inspector would take the mechanical teacher away, just as Tommy's teacher was once taken away for a month.",
        "evidence": "Book Page 47 Exercise A.3: 'She had been hoping they would take the teacher away altogether.'"
    },
    {
        "page": 47,
        "question": "Identify the character or speaker: They learned the same things, so they could help one another with the home work and talk about it.",
        "aliases": [
            "they learned the same things so they could help one another",
            "help one another with the homework the fun they had"
        ],
        "direct_answer": "Margie",
        "completed_sentence": "Character / Speaker: **[Margie]**.",
        "explanation": "Margie reflected wistfully on how centuries ago, school children learned together and helped each other.",
        "evidence": "Book Page 47 Exercise A.4: 'They learned the same things, so they could help one another with the home work and talk about it.'"
    },
    {
        "page": 47,
        "question": "Identify the character or speaker: They had a special building and all the kids went there.",
        "aliases": [
            "they had a special building and all the kids went there",
            "special building and all the kids went there"
        ],
        "direct_answer": "Tommy",
        "completed_sentence": "Character / Speaker: **[Tommy]**.",
        "explanation": "Tommy explained to Margie that old schools were separate buildings where children gathered, rather than bedrooms at home.",
        "evidence": "Book Page 47 Exercise A.5: 'They had a special building and all the kids went there.'"
    },
    {
        "page": 47,
        "question": "Fill in the blanks with the clues given below to complete the paragraph: The Fun They Had",
        "aliases": [
            "fill in the blanks with the clues given below to complete the paragraph the fun they had",
            "tommy and margie found something about the old schools",
            "paragraph clues the fun they had"
        ],
        "direct_answer": "(i) schools | (ii) real book | (iii) attic | (iv) yellow and crinkly | (v) words | (vi) millions of books | (vii) geography | (viii) test papers | (ix) house | (x) school time | (xi) person | (xii) same thing | (xiii) learning and spending",
        "completed_sentence": "Tommy and Margie found something about the (i) **[schools]** of the past. Tommy found a (ii) **[real book]** in the (iii) **[attic]**. The pages were (iv) **[yellow and crinkly]**. The (v) **[words]** stood still unlike screens holding (vi) **[millions of books]**. Margie struggled with tests in (vii) **[geography]** on punch code (viii) **[test papers]**. Her school was in her (ix) **[house]** at fixed (x) **[school time]**. Tommy explained old teachers were a (xi) **[person]**, teaching the (xii) **[same thing]** where kids enjoyed (xiii) **[learning and spending]** time together.",
        "explanation": "Official paragraph completion exercise from Unit 2: The Fun They Had (Page 47).",
        "evidence": "Book Page 47 Exercise B: Fill in the blanks with the clues given below to complete the paragraph."
    },
    {
        "page": 48,
        "question": "The old book was found by ___________________________________",
        "aliases": [
            "the old book was found by",
            "who found the old book the fun they had"
        ],
        "direct_answer": "Tommy in the attic of his house.",
        "completed_sentence": "The old book was found by **[Tommy in the attic of his house]**.",
        "explanation": "On 17 May 2157, Margie wrote in her diary that Tommy found a real printed book in his attic.",
        "evidence": "Book Page 48 Exercise C.1: 'The old book was found by ___________________________'"
    },
    {
        "page": 48,
        "question": "Margie was surprised to see the book because __________________",
        "aliases": [
            "margie was surprised to see the book because",
            "why was margie surprised to see the book"
        ],
        "direct_answer": "the words stood still on yellow, crinkly pages instead of moving on a television screen.",
        "completed_sentence": "Margie was surprised to see the book because **[the words stood completely still on paper instead of moving on a screen]**.",
        "explanation": "Margie had only experienced telebooks where words scrolled on screen, so static text on paper was strange to her.",
        "evidence": "Book Page 48 Exercise C.2: 'Margie was surprised to see the book because __________________'"
    },
    {
        "page": 48,
        "question": "The mechanical teacher had been giving her ____________________",
        "aliases": [
            "the mechanical teacher had been giving her",
            "mechanical teacher had been giving margie"
        ],
        "direct_answer": "test after test in geography.",
        "completed_sentence": "The mechanical teacher had been giving her **[test after test in geography]**.",
        "explanation": "Margie had been doing worse and worse because the geography sector had been geared too quickly.",
        "evidence": "Book Page 48 Exercise C.3: 'The mechanical teacher had been giving her ____________________'"
    },
    {
        "page": 48,
        "question": "Margie’s schoolroom was right next to ________________________",
        "aliases": [
            "margies schoolroom was right next to",
            "where was margies schoolroom"
        ],
        "direct_answer": "her bedroom.",
        "completed_sentence": "Margie's schoolroom was right next to **[her bedroom]**.",
        "explanation": "Margie attended individual home schooling where her mechanical teacher waited in the room next to her bedroom.",
        "evidence": "Book Page 48 Exercise C.5: 'Margie’s schoolroom was right next to ________________________'"
    },
    {
        "page": 77,
        "question": "Based on the understanding of the poem, write down the summary of the poem by filling in the blanks: On Killing a Tree",
        "aliases": [
            "summary of on killing a tree",
            "write down the summary of the poem by filling in the blanks on killing a tree",
            "the poet explains the process of killing a tree",
            "complete the summary on killing a tree"
        ],
        "direct_answer": "1. killing a tree | 2. kill it | 3. a knife (a simple jab of the knife) | 4. sunlight, air and water | 5. bleeding bark | 6. green twigs | 7. miniature boughs | 8. kill it | 9. sun and air (scorching and choking)",
        "completed_sentence": "The poet explains the process of **[killing a tree]**. A lot of work has to be done to **[kill it]** completely. It cannot be accomplished by merely cutting it with **[a knife]**. The tree has grown strong with **[sunlight, air and water]**. Even the **[bleeding bark]** gives rise to **[green twigs]**. The **[miniature boughs]** sprout new leaves. To **[kill it]** completely, one should pull out its roots from the soil and expose them to **[sun and air]**.",
        "explanation": "Official complete textbook summary fill-in-the-blanks exercise from Unit 3: On Killing a Tree (Page 77).",
        "evidence": "Book Page 77 Exercise C: Based on the understanding of the poem, write down the summary of the poem by filling in the blanks."
    },
    {
        "page": 77,
        "question": "Why should the root be pulled out? On Killing a Tree",
        "aliases": [
            "why should the root be pulled out",
            "why root must be pulled out on killing a tree"
        ],
        "direct_answer": "To completely kill the tree, because the root is its hidden strength and source of life that allows it to regenerate if left in the ground.",
        "completed_sentence": "The root must be pulled out **[to completely destroy the tree's hidden strength and prevent it from sprouting again]**.",
        "explanation": "The root is the sensitive, white, and wet anchor deep in the earth; only complete uprooting terminates its life.",
        "evidence": "Book Page 77 Exercise 5.i: 'Why should the root be pulled out?'"
    },
    {
        "page": 77,
        "question": "What does ‘anchoring earth’ mean? On Killing a Tree",
        "aliases": [
            "what does anchoring earth mean",
            "anchoring earth meaning on killing a tree"
        ],
        "direct_answer": "It means the soil holds the roots firmly and securely, providing support and nourishment like an anchor holds a ship.",
        "completed_sentence": "Anchoring earth means **[the soil that securely holds the roots of the tree, providing life and stability]**.",
        "explanation": "Metaphor comparing the earth gripping the roots to a ship's anchor holding fast to the seabed.",
        "evidence": "Book Page 77 Exercise 5.ii: 'What does ‘anchoring earth’ mean?'"
    },
    {
        "page": 77,
        "question": "What does the poet mean by ‘bleeding bark’? On Killing a Tree",
        "aliases": [
            "what does the poet mean by bleeding bark",
            "bleeding bark meaning on killing a tree"
        ],
        "direct_answer": "The sap oozing out of the cut trunk when hacked, compared to blood flowing from a human wound.",
        "completed_sentence": "Bleeding bark refers to **[the sap flowing out from the wounded trunk when hacked with a knife]**.",
        "explanation": "Gieve Patel uses personification and vivid metaphor to convey the tree's suffering.",
        "evidence": "Book Page 77 Exercise D.4: 'What does the poet mean by ‘bleeding bark’?'"
    },
    {
        "page": 86,
        "question": "Fill in the blanks with words from the text: Earthquake",
        "aliases": [
            "fill in the blanks with words from the text earthquake",
            "earthquake fill in the blanks",
            "the name of the narrator is brij",
            "page 86 fill in the blanks"
        ],
        "direct_answer": "1. Brij | 2. six hundred and seventy (670) | 3. school books | 4. makeshift hospital | 5. a hundred and sixteen (116)",
        "matches": [
            [
                "1. The name of the narrator is",
                "Brij"
            ],
            [
                "2. There were ... villages in the valley",
                "six hundred and seventy (670)"
            ],
            [
                "3. Brij went to Pauri to buy his",
                "school books"
            ],
            [
                "4. The soldiers had set up a",
                "makeshift hospital"
            ],
            [
                "5. Bhuli had been buried under the debris for",
                "a hundred and sixteen (116) hours"
            ]
        ],
        "completed_sentence": "Earthquake Blanks: **[1. Brij, 2. six hundred and seventy (670), 3. school books, 4. makeshift hospital, 5. a hundred and sixteen (116) hours]**.",
        "explanation": "Official fill in the blanks exercise from Unit 3 Supplementary: Earthquake (Page 86).",
        "evidence": "Book Page 86 Exercise A: Fill in the blanks with words from the text."
    },
    {
        "page": 86,
        "question": "The name of the narrator is",
        "aliases": [
            "the name of the narrator is",
            "name of narrator earthquake"
        ],
        "direct_answer": "Brij",
        "completed_sentence": "The name of the narrator is **[Brij]**.",
        "explanation": "Brij runs a teashop in Garhwal and narrates his survival during the devastating earthquake.",
        "evidence": "Book Page 86 Exercise A.1: 'The name of the narrator is Brij.'"
    },
    {
        "page": 86,
        "question": "There were ____________ villages in the valley. Earthquake",
        "aliases": [
            "there were villages in the valley",
            "how many villages in the valley earthquake"
        ],
        "direct_answer": "six hundred and seventy (670)",
        "completed_sentence": "There were **[six hundred and seventy (670)]** villages in the valley.",
        "explanation": "The valley had 670 villages, of which 602 were completely destroyed by the tremors.",
        "evidence": "Book Page 86 Exercise A.2: 'There were six hundred and seventy villages in the valley.'"
    },
    {
        "page": 86,
        "question": "Brij went to Pauri to buy his",
        "aliases": [
            "brij went to pauri to buy his",
            "why did brij go to pauri"
        ],
        "direct_answer": "school books",
        "completed_sentence": "Brij went to Pauri to buy his **[school books]**.",
        "explanation": "Brij was away in Pauri purchasing books when the earthquake struck Molthi, which saved his life.",
        "evidence": "Book Page 86 Exercise A.3: 'Brij went to Pauri to buy his school books.'"
    },
    {
        "page": 86,
        "question": "The soldiers had set up a",
        "aliases": [
            "the soldiers had set up a",
            "soldiers set up earthquake"
        ],
        "direct_answer": "makeshift hospital",
        "completed_sentence": "The soldiers had set up a **[makeshift hospital]** in a tent.",
        "explanation": "Army rescue teams treated injured victims in a makeshift hospital camp.",
        "evidence": "Book Page 86 Exercise A.4: 'The soldiers had set up a makeshift hospital.'"
    },
    {
        "page": 86,
        "question": "Bhuli had been buried under the debris for ____________ hours",
        "aliases": [
            "bhuli had been buried under the debris for hours",
            "how many hours bhuli buried"
        ],
        "direct_answer": "a hundred and sixteen (116) hours",
        "completed_sentence": "Bhuli had been buried under the debris for **[a hundred and sixteen (116)]** hours.",
        "explanation": "Miraculously, baby Bhuli survived over four days (116 hours) trapped beneath a caved-in door.",
        "evidence": "Book Page 86 Exercise A.5: 'Bhuli had been buried under the debris for a hundred and sixteen hours.'"
    },
    {
        "page": 113,
        "question": "Based on your reading, rearrange the following sentences in the correct sequence: The Cat and the Pain-Killer",
        "aliases": [
            "rearrange the following sentences in the correct sequence the cat and the pain killer",
            "rearrange sentences the cat and the pain killer",
            "correct sequence tom sawyer cat painkiller",
            "order the sentences page 113"
        ],
        "direct_answer": "Correct Sequence: 5, 8, 1, 7, 3, 4, 6, 2",
        "matches": [
            [
                "1st (5)",
                "Tom was dull and depressed."
            ],
            [
                "2nd (8)",
                "So, Aunt Polly tried different types of remedies on him."
            ],
            [
                "3rd (1)",
                "Since all her methods failed, finally she gave him a pain-killer."
            ],
            [
                "4th (7)",
                "But, Tom gave that pain-killer to the cat Peter."
            ],
            [
                "5th (3)",
                "The pain-killer triggered adverse reactions on Peter."
            ],
            [
                "6th (4)",
                "It jumped out of the open window."
            ],
            [
                "7th (6)",
                "This incident upset Aunt Polly and she questioned him."
            ],
            [
                "8th (2)",
                "He told his aunt that Peter had no aunt, so he gave him the medicine."
            ]
        ],
        "completed_sentence": "Ordered Sequence: **[5 ➔ 8 ➔ 1 ➔ 7 ➔ 3 ➔ 4 ➔ 6 ➔ 2]**.",
        "explanation": "Official chronological ordering exercise from Unit 4 Supplementary: The Cat and the Pain-Killer (Page 113).",
        "evidence": "Book Page 113 Exercise C: Based on your reading, rearrange the following sentences in the correct sequence."
    },
    {
        "page": 113,
        "question": "Complete the summary of the extract using the appropriate words from the box below: The Cat and the Pain-Killer",
        "aliases": [
            "complete the summary of the extract using the appropriate words from the box below",
            "the cat and the pain killer summary",
            "tom sawyer felt dejected as becky thatcher had stopped coming to school",
            "fill in the blanks cat and the pain killer page 113 114"
        ],
        "direct_answer": "1. dejected | 2. school | 3. health | 4. remedies | 5. pretended | 6. crack | 7. Peter | 8. pain-killer | 9. summersets | 10. teaspoon | 11. cruelty | 12. stopped",
        "completed_sentence": "Tom Sawyer felt **[dejected]** as Becky Thatcher had stopped coming to **[school]**. Aunt Polly was concerned about his **[health]** condition. So, she tried various **[remedies]** on him. Tom **[pretended]** to like the pain-killer and mended the **[crack]** on the floor with it. One day, Tom gave the pain-killer to Aunt's cat, **[Peter]**. The **[pain-killer]** had an adverse effect on the cat. Aunt Polly saw the cat throw **[summersets]** and sail through the window. She found the **[teaspoon]** and realized what was **[cruelty]** to the cat was the same to the boy and **[stopped]** giving medicines to him.",
        "explanation": "Official complete textbook summary fill-in-the-blanks exercise from Unit 4: The Cat and the Pain-Killer (Pages 113-114).",
        "evidence": "Book Page 113-114 Exercise F: Complete the summary of the extract using the appropriate words from the box below."
    },
    {
        "page": 113,
        "question": "Why did Tom lose the charm of his life? The Cat and the Pain-Killer",
        "aliases": [
            "why did tom lose the charm of his life",
            "tom lost the charm of his life because"
        ],
        "direct_answer": "Because his friend Becky Thatcher had fallen ill and stopped coming to school.",
        "completed_sentence": "Tom lost the charm of his life because **[Becky Thatcher stopped coming to school]**.",
        "explanation": "Her absence caused Tom to feel depressed, abandon play, and mope around the house.",
        "evidence": "Book Page 113 Exercise D.1: 'Why did Tom lose the charm of his life?'"
    },
    {
        "page": 113,
        "question": "Why did Aunt Polly try different remedies on Tom?",
        "aliases": [
            "why did aunt polly try different remedies on tom",
            "why aunt polly gave remedies to tom"
        ],
        "direct_answer": "Because Tom was moping, sad, and silent, and Aunt Polly was an incurable experimenter in quack health remedies.",
        "completed_sentence": "Aunt Polly tried remedies because **[she was determined to cure Tom's moping and infatuation with health treatises]**.",
        "explanation": "She subjected him to cold-water baths, hot baths, blister plasters, and bitter concoctions to revive his spirits.",
        "evidence": "Book Page 113 Exercise D.2: 'Why did Aunt Polly try different remedies on Tom?'"
    },
    {
        "page": 113,
        "question": "How did the medicine diminish? The Cat and the Pain-Killer",
        "aliases": [
            "how did the medicine diminish",
            "how medicine diminished tom sawyer"
        ],
        "direct_answer": "Tom secretly poured teaspoonfuls of the pain-killer into a crack in the sitting-room floor.",
        "completed_sentence": "The medicine diminished because **[Tom poured it into a crack in the sitting-room floor every day]**.",
        "explanation": "Tom pretended to love the pain-killer so his aunt would leave the bottle with him, but he fed the floor crack instead.",
        "evidence": "Book Page 113 Exercise D.3: 'How did the medicine diminish?'"
    },
    {
        "page": 113,
        "question": "Did Tom compel Peter to have the pain-killer?",
        "aliases": [
            "did tom compel peter to have the pain killer",
            "did tom force the cat to have painkiller"
        ],
        "direct_answer": "No, Peter begged for it with eager purrs and rubbed against Tom's legs, though Tom willingly poured it into his mouth.",
        "completed_sentence": "No, Tom did not compel Peter; **[Peter begged for it by nudging the spoon and purring]**.",
        "explanation": "Tom warned the cat that it was fiery stuff, but Peter persisted in wanting a taste.",
        "evidence": "Book Page 113 Exercise D.4: 'Did Tom compel Peter to have the pain-killer?'"
    },
    {
        "page": 113,
        "question": "How did Aunt Polly discover the reason for Peter’s absurd behaviour?",
        "aliases": [
            "how did aunt polly discover the reason for peters absurd behaviour",
            "how aunt polly found out about peter"
        ],
        "direct_answer": "She spotted the teaspoon handle sticking out from beneath the bed valance and questioned Tom.",
        "completed_sentence": "Aunt Polly discovered the reason when **[she bent down and saw the teaspoon handle under the bed valance]**.",
        "explanation": "Picking up the spoon and smelling it, she realized Tom had fed the pain-killer to Peter.",
        "evidence": "Book Page 113 Exercise D.6: 'How did Aunt Polly discover the reason for Peter’s absurd behaviour?'"
    },
    {
        "page": 113,
        "question": "What was the reason given by Tom for giving the pain-killer to the cat?",
        "aliases": [
            "what was the reason given by tom for giving the pain killer to the cat",
            "toms reason for giving pain killer to cat"
        ],
        "direct_answer": "Tom said he did it out of pity because Peter had no aunt to roast his bowels out with remedies.",
        "completed_sentence": "Tom explained that **[he felt sorry for Peter because Peter had no aunt to roast his bowels out and treat him without thinking]**.",
        "explanation": "Tom used the witty retort to make Aunt Polly realize how cruel her remedies were.",
        "evidence": "Book Page 113 Exercise D.7: 'What was the reason given by Tom for giving the pain-killer to the cat?'"
    },
    {
        "page": 113,
        "question": "Why did Aunt Polly’s eyes water? The Cat and the Pain-Killer",
        "aliases": [
            "why did aunt pollys eyes water",
            "why aunt pollys eyes watered"
        ],
        "direct_answer": "She felt remorse, sympathy, and sudden realization that forcing bitter medicines on Tom was just as cruel as doing it to the cat.",
        "completed_sentence": "Aunt Polly's eyes watered because **[she felt remorse and sympathy upon realizing how cruel her dosing had been to Tom]**.",
        "explanation": "She placed her hand on Tom's head and told him she meant it for his good, and stopped giving him medicine.",
        "evidence": "Book Page 113 Exercise D.8: 'Why did Aunt Polly’s eyes water?'"
    },
    {
        "page": 114,
        "question": "Convert the American slang usage in The Cat and the Pain-Killer to standard English",
        "aliases": [
            "american slang usage of english complete the tabular column with standard english",
            "american slang the cat and the pain killer",
            "american slang standard english page 114"
        ],
        "direct_answer": "1. Finally hit ‘pon ➔ Finally hit upon / thought of | 2. There ain’t anything mean about me ➔ There isn’t anything mean about me | 3. ‘Deed I don’t know ➔ Indeed I don’t know | 4. Yes’m. That is, I believe they do ➔ Yes, ma'am. That is, I believe they do | 5. ‘She’d a roasted bowel out of me.’ ➔ She would have roasted the bowels out of me | 6. ‘Oh, go ‘long with you, Tom.’ ➔ Oh, go along with you, Tom",
        "matches": [
            [
                "1. Finally hit ‘pon",
                "Finally hit upon / thought of"
            ],
            [
                "2. There ain’t anything mean about me",
                "There isn’t anything mean about me"
            ],
            [
                "3. ‘Deed I don’t know",
                "Indeed I don’t know"
            ],
            [
                "4. Yes’m. That is, I believe they do",
                "Yes, ma'am. That is, I believe they do"
            ],
            [
                "5. ‘She’d a roasted bowel out of me.’",
                "She would have roasted the bowels out of me"
            ],
            [
                "6. ‘Oh, go ‘long with you, Tom.’",
                "Oh, go along with you, Tom"
            ]
        ],
        "completed_sentence": "American Slang to Standard English: **[Finally hit 'pon ➔ hit upon, ain't ➔ isn't, 'Deed ➔ Indeed, Yes'm ➔ Yes ma'am, She'd a ➔ She would have, go 'long ➔ go along]**.",
        "explanation": "Official American slang conversion table from Unit 4: The Cat and the Pain-Killer (Page 114).",
        "evidence": "Book Page 114 Exercise G: In the story we find a lot of American slang usage of English. Complete the tabular column with standard English."
    }
]

if __name__ == '__main__':
    with open('mobile_app/assets/qa_bank.json', 'w', encoding='utf-8') as f:
        json.dump(qa_list, f, indent=2, ensure_ascii=False)
    print(f"Total comprehensive Q&A items: {len(qa_list)}")
    print("Updated mobile_app/assets/qa_bank.json successfully!")
