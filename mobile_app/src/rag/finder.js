// On-device High-Accuracy RAG & Interactive Page Explorer for English Class 9 Textbook
import chunks from '../../assets/chunks.json';
import qaBank from '../../assets/qa_bank.json';
import pageIndex from '../../assets/page_index.json';

const STOP = new Set(
  "a an the is are was were of for to in on at and or do does did i my me you your what whats how can could when who whom which where there it be been with about tell please much many have has had will would if any get this that these those from by"
    .split(" ")
);

function getWords(text) {
  if (!text) return [];
  const matches = (text.toLowerCase().match(/[a-z0-9]+/g) || []);
  return matches.filter((w) => !STOP.has(w) && w.length > 2);
}

function normalize(text) {
  return (text || "").toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ").trim();
}

// Strictly isolated subject domain boundaries to prevent cross-lesson hallucinations (e.g. Sachin)
const DOMAINS = {
  sachin: ["sachin", "tendulkar", "cricket", "achrekar", "ajit", "shivaji", "shardashram", "vadapav", "gavaskar", "stumps", "nets", "batting", "bowled"],
  cat: ["cat", "painkiller", "pain-killer", "peter", "aunt polly", "polly", "tom", "tom sawyer", "thimble", "somersaults", "becky", "teaspoon", "crack"],
  oranges: ["orange", "oranges", "seventeen", "pongo", "clem", "docks", "steal", "stolen", "pips", "peel", "apron", "cheese", "swift delivery", "scotti"],
  spider: ["spider", "fly", "parlour", "web", "gauzy", "flattery", "flatter", "cunning", "trust", "betray", "winding stair", "den"],
  river: ["river", "flood", "amy", "betty", "rose", "sara", "jim", "cloudburst", "splint", "ladder", "red cross", "stream", "pebble", "burnett"],
  tree: ["visitor", "ruskin", "bond", "jackfruit", "iron cross", "granite", "climb", "trees", "pruning", "chiming", "turnstile"],
  water: ["water", "elixir", "raman", "nile", "egypt", "silt", "soil", "erosion", "amrita", "landscape", "rainfed", "afforestation", "forests"],
  killing_tree: ["killing a tree", "bleeding bark", "anchoring earth", "jab", "hack", "chop", "sprout", "miniature boughs", "uprooted"],
  earthquake: ["earthquake", "brij", "bhuli", "molthi", "pauri", "debris", "tremor", "teashop", "traveller", "army officer"],
  woods: ["woods", "snowy", "evening", "miles to go", "robert frost", "harness bells", "queer", "frozen lake", "farmhouse"],
  poison: ["poison tree", "wrath", "foe", "apple bright", "fears", "tears", "blake"],
  fun_had: ["margie", "tommy", "mechanical teacher", "county inspector", "geography", "attic", "telebook", "real book"]
};

function hasKeyword(query, kwList) {
  const q = query.toLowerCase();
  return kwList.some((kw) => q.includes(kw));
}

/**
 * Checks if the user is asking to browse/list questions by page number or unit.
 * E.g., "Page 33", "Book Page 6", "Unit 2", "Page 106", "p 33", "33", "Unit 4"
 */
export function checkPageOrUnitRequest(query) {
  if (!query || !query.trim()) return null;
  const q = query.toLowerCase().trim();

  // 1. Page match: "page 106", "p 106", "p. 106", "book page 106", "106"
  const pageMatch = q.match(/(?:book\s+)?(?:page|p\.?)\s*([0-9]{1,3})/i) || q.match(/^([0-9]{1,3})$/);
  if (pageMatch) {
    const pageNo = pageMatch[1];
    if (pageIndex.pages && pageIndex.pages[pageNo]) {
      const data = pageIndex.pages[pageNo];
      return {
        isQuestionPicker: true,
        type: 'page',
        page: pageNo,
        unit: data.unit,
        title: data.title,
        questions: data.questions,
      };
    } else {
      // Graceful directory for any page
      return {
        isQuestionPicker: true,
        type: 'page',
        page: pageNo,
        unit: 'Tamil Nadu English Class 9',
        title: `Book Page ${pageNo}`,
        questions: [
          `Read key excerpts from Book Page ${pageNo}`,
          `Explain the main lesson concepts on Page ${pageNo}`,
          `Browse Unit 4 Listening Exercises (Book Page 106)`,
          `Browse Unit 2 (Book Page 33)`,
          `Browse Unit 1 (Book Page 6)`
        ],
      };
    }
  }

  // 2. Unit match: "unit 1", "unit 2", "unit 4", "unit 5"
  const unitMatch = q.match(/unit\s*([0-9]+)/i);
  if (unitMatch) {
    const unitId = parseInt(unitMatch[1], 10);
    const unitInfo = pageIndex.units.find((u) => u.id === unitId);
    if (unitInfo) {
      const unitQuestions = [];
      unitInfo.pages.forEach((p) => {
        const pStr = p.toString();
        if (pageIndex.pages[pStr] && pageIndex.pages[pStr].questions) {
          pageIndex.pages[pStr].questions.forEach((qItem) => {
            if (!unitQuestions.includes(qItem)) {
              unitQuestions.push(qItem);
            }
          });
        }
      });

      return {
        isQuestionPicker: true,
        type: 'unit',
        unit: unitInfo.title,
        title: `Pages ${unitInfo.pages[0]} to ${unitInfo.pages[unitInfo.pages.length - 1]}`,
        questions: unitQuestions,
      };
    }
  }

  return null;
}

/**
 * Searches the English Class 9 textbook with high precision:
 * Tier 0: Interactive Page & Unit Question Directory Picker.
 * Tier 1: Verified Comprehension & Exercise Q&A Bank (Direct Answers, Highlighted Blanks, Matching).
 * Tier 2: Domain-Isolated Precision Chunk Search over 1,137 textbook chunks.
 */
export function findFact(question) {
  if (!question || !question.trim()) return null;

  // ----------------------------------------------------
  // TIER 0: Page or Unit Directory Request
  // ----------------------------------------------------
  const pickerResult = checkPageOrUnitRequest(question);
  if (pickerResult) {
    return pickerResult;
  }

  const qNorm = normalize(question);
  const qWords = getWords(question);
  if (qWords.length === 0) return null;
  const qWordSet = new Set(qWords);

  // ----------------------------------------------------
  // TIER 1: Comprehension & Exercise Q&A Bank Match
  // ----------------------------------------------------
  // 1a. Exact alias match
  for (const item of qaBank) {
    if (item.aliases) {
      for (const alias of item.aliases) {
        if (qNorm === normalize(alias)) {
          return {
            isDirectQA: true,
            structured: item,
            answer: item.direct_answer,
            page: item.page,
            evidence: item.evidence,
          };
        }
      }
    }
  }

  // 1b. Exact question match
  for (const item of qaBank) {
    if (qNorm === normalize(item.question)) {
      return {
        isDirectQA: true,
        structured: item,
        answer: item.direct_answer,
        page: item.page,
        evidence: item.evidence,
      };
    }
  }

  // 1c. Strict entity-isolated semantic match
  let bestItem = null;
  let bestScore = 0;

  for (const item of qaBank) {
    const itemQ = item.question.toLowerCase();

    // Entity Boundary Isolation - Sachin Tendulkar should never answer non-cricket questions
    if (hasKeyword(itemQ, DOMAINS.sachin) && !hasKeyword(question, DOMAINS.sachin)) continue;
    if (hasKeyword(question, DOMAINS.sachin) && !hasKeyword(itemQ, DOMAINS.sachin)) continue;

    const itemWords = new Set([
      ...getWords(item.question),
      ...(item.aliases ? item.aliases.flatMap(getWords) : [])
    ]);

    let overlap = 0;
    for (const w of qWords) {
      if (itemWords.has(w)) overlap++;
    }

    const coverage = overlap / qWords.length;
    let score = overlap * (1 + coverage);

    // Boost for exercise types
    if ((qWordSet.has("match") || qWordSet.has("following")) && item.matches) {
      score += 15;
    }
    if ((qWordSet.has("blank") || qWordSet.has("blanks") || qWordSet.has("fill")) && item.completed_sentence) {
      score += 10;
    }
    if ((qWordSet.has("rearrange") || qWordSet.has("sequence")) && item.matches) {
      score += 15;
    }
    if ((qWordSet.has("true") || qWordSet.has("false")) && item.question.toLowerCase().includes("true")) {
      score += 15;
    }

    if ((overlap >= 3 || (overlap >= 2 && coverage >= 0.35)) && score > bestScore) {
      bestScore = score;
      bestItem = item;
    }
  }

  if (bestItem) {
    return {
      isDirectQA: true,
      structured: bestItem,
      answer: bestItem.direct_answer,
      page: bestItem.page,
      evidence: bestItem.evidence,
    };
  }

  // ----------------------------------------------------
  // TIER 2: Precision Chunk Search over 1,137 Textbook Chunks
  // ----------------------------------------------------
  let bestChunk = null;
  let bestChunkScore = 0;

  for (const ch of chunks) {
    // Only isolate Sachin to avoid cricket contaminating unrelated literature
    if (ch.topic === "sachin_cricket" && !hasKeyword(question, DOMAINS.sachin)) continue;
    if (hasKeyword(question, DOMAINS.sachin) && ch.topic !== "sachin_cricket") continue;

    const chWordSet = new Set(ch.keywords || []);
    let matchCount = 0;
    for (const qw of qWords) {
      if (chWordSet.has(qw)) matchCount++;
    }

    if (matchCount === 0) continue;

    let score = matchCount * 2.0;

    // Topic boost if user query matches domain keywords
    if (ch.topic === "cat_painkiller" && hasKeyword(question, DOMAINS.cat)) score += 10.0;
    if (ch.topic === "seventeen_oranges" && hasKeyword(question, DOMAINS.oranges)) score += 10.0;
    if (ch.topic === "spider_fly" && hasKeyword(question, DOMAINS.spider)) score += 10.0;
    if (ch.topic === "old_man_river" && hasKeyword(question, DOMAINS.river)) score += 10.0;
    if (ch.topic === "water_elixir" && hasKeyword(question, DOMAINS.water)) score += 10.0;
    if (ch.topic === "ruskin_tree" && hasKeyword(question, DOMAINS.tree)) score += 10.0;
    if (ch.topic === "sachin_cricket" && hasKeyword(question, DOMAINS.sachin)) score += 10.0;

    if (score > bestChunkScore) {
      bestChunkScore = score;
      bestChunk = ch;
    }
  }

  if (bestChunk && bestChunkScore >= 2.0) {
    return {
      isDirectQA: false,
      chunk: bestChunk.text,
      page: bestChunk.page,
      unit: bestChunk.unit_title,
    };
  }

  // Tier 3: Guaranteed fallback chunk so SLM always has textbook grounding
  if (bestChunk) {
    return {
      isDirectQA: false,
      chunk: bestChunk.text,
      page: bestChunk.page,
      unit: bestChunk.unit_title,
    };
  }

  const defaultChunk = chunks.find(c => c.topic !== "sachin_cricket") || chunks[0];
  return {
    isDirectQA: false,
    chunk: defaultChunk.text,
    page: defaultChunk.page,
    unit: defaultChunk.unit_title,
  };
}
