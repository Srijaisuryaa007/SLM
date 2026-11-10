// On-device RAG search & Interactive Page Explorer for English Class 9 Textbook
import bookPages from '../../assets/facts.json';
import qaBank from '../../assets/qa_bank.json';
import pageIndex from '../../assets/page_index.json';

const STOP = new Set(
  "a an the is are was were of for to in on at and or do does did i my me you your what whats how can could when who whom which where there it be been with about tell please much many have has had will would if any get this that these those from by"
    .split(" ")
);

function getWords(text) {
  if (!text) return [];
  const matches = (text.toLowerCase().match(/[a-z0-9]+/g) || []);
  return matches.filter((w) => !STOP.has(w));
}

function normalize(text) {
  return (text || "").toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ").trim();
}

/**
 * Checks if the user is asking to browse/list questions by page number or unit.
 * E.g., "Page 33", "Book Page 6", "Unit 2", "Page 118", "p 33", "33", "Unit 4"
 */
export function checkPageOrUnitRequest(query) {
  if (!query || !query.trim()) return null;
  const q = query.toLowerCase().trim();

  // 1. Page match: "page 33", "p 33", "p. 33", "book page 33", "33"
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
    }
  }

  // 2. Unit match: "unit 1", "unit 2", "unit 4", "unit 5"
  const unitMatch = q.match(/unit\s*([0-9]+)/i);
  if (unitMatch) {
    const unitId = parseInt(unitMatch[1], 10);
    const unitInfo = pageIndex.units.find((u) => u.id === unitId);
    if (unitInfo) {
      // Collect questions from all pages of this unit
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
        title: `By ${unitInfo.author} (Pages ${unitInfo.pages.join(', ')})`,
        questions: unitQuestions,
      };
    }
  }

  return null;
}

/**
 * Searches the English Class 9 textbook:
 * Tier 0: Page / Unit / Part Number Question Directory (Interactive Question Picker).
 * Tier 1: Comprehension & Exercise Q&A Bank (Direct verified answer + textbook proof).
 * Tier 2: Story Reading Prose Sliding Window search for freeform questions.
 */
export function findFact(question) {
  if (!question || !question.trim()) return null;

  // ----------------------------------------------------
  // TIER 0: Page or Unit Question Browser
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
  // TIER 1: Comprehension Q&A Bank Match
  // ----------------------------------------------------
  // 1a. Exact alias match
  for (const item of qaBank) {
    if (item.aliases) {
      for (const alias of item.aliases) {
        if (qNorm === normalize(alias)) {
          return {
            isDirectQA: true,
            structured: item,
            answer: item.answer,
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
        answer: item.answer,
        page: item.page,
        evidence: item.evidence,
      };
    }
  }

  // 1c. Intelligent keyword / alias / match-the-following overlap
  let bestItem = null;
  let bestScore = 0;

  for (const item of qaBank) {
    const qTargets = new Set(getWords(item.question));
    const aliasTargets = new Set();
    if (item.aliases) {
      for (const a of item.aliases) {
        getWords(a).forEach((w) => aliasTargets.add(w));
      }
    }

    const matchKeys = new Set();
    if (item.matches) {
      for (const [k, v] of item.matches) {
        getWords(k).forEach((w) => matchKeys.add(w));
        getWords(v).forEach((w) => matchKeys.add(w));
      }
    }

    const allItemWords = new Set([...qTargets, ...aliasTargets, ...matchKeys]);
    let score = 0;
    for (const w of qWords) {
      if (allItemWords.has(w)) score++;
    }

    // Boost score if question asks to "match" and contains match keys
    if ((qWordSet.has("match") || qWordSet.has("following")) && item.matches) {
      let matchedCount = 0;
      for (const w of qWords) {
        if (matchKeys.has(w)) matchedCount++;
      }
      if (matchedCount >= 2) score += 10;
    }

    if (score > bestScore && score >= 2) {
      bestScore = score;
      bestItem = item;
    }
  }

  if (bestItem) {
    return {
      isDirectQA: true,
      structured: bestItem,
      answer: bestItem.answer,
      page: bestItem.page,
      evidence: bestItem.evidence,
    };
  }

  // ----------------------------------------------------
  // TIER 2: Story Reading Prose Sliding Window Search
  // ----------------------------------------------------
  let bestChunk = null;
  let bestStoryScore = 0;
  let bestPage = null;

  for (const page of bookPages) {
    const text = page.text || "";
    if (!text) continue;

    // Skip exercise/multiple choice tables from matching as story facts
    if (text.includes("a) ") && text.includes("b) ") && text.includes("c) ")) {
      continue;
    }

    const sentences = text.split(/(?<=[.!?])\s+/);
    for (let i = 0; i < sentences.length; i++) {
      const chunk = sentences.slice(i, i + 4).join(" ");
      const cWords = new Set(getWords(chunk));

      let score = 0;
      for (const w of qWords) {
        if (cWords.has(w)) score++;
      }

      if (score > bestStoryScore) {
        bestStoryScore = score;
        bestChunk = chunk;
        bestPage = page.book_page;
      }
    }
  }

  if (bestStoryScore >= 2 && bestChunk) {
    return {
      isDirectQA: false,
      chunk: bestChunk,
      page: bestPage,
    };
  }

  return null;
}
