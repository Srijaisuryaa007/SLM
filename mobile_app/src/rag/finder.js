// On-device RAG search for English Class 9 Textbook
import bookPages from '../../assets/facts.json';
import qaBank from '../../assets/qa_bank.json';

const STOP = new Set(
  "a an the is are was were of for to in on at and or do does did i my me you your what whats how can could when who whom which where there it be been with about tell please much many have has had will would if any get this that these those from by"
    .split(" ")
);

function getWords(text) {
  if (!text) return [];
  const matches = text.toLowerCase().match(/[a-z0-9]+/g) || [];
  return matches.filter((w) => !STOP.has(w));
}

function normalize(text) {
  return (text || "").toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ").trim();
}

/**
 * Searches the English Class 9 textbook:
 * Tier 1: Comprehension Q&A Bank (Direct verified answer + textbook evidence).
 * Tier 2: Story Prose Sliding Window search for freeform questions.
 */
export function findFact(question) {
  if (!question || !question.trim()) return null;

  const qNorm = normalize(question);
  const qWords = getWords(question);
  if (qWords.length === 0) return null;

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
        answer: item.answer,
        page: item.page,
        evidence: item.evidence,
      };
    }
  }

  // 1c. High-confidence question keyword overlap (>= 75% question words match)
  let bestQA = null;
  let bestQAScore = 0;
  for (const item of qaBank) {
    const targetWords = new Set(getWords(item.question));
    let matchCount = 0;
    for (const w of qWords) {
      if (targetWords.has(w)) matchCount++;
    }
    const ratio = matchCount / qWords.length;
    if (ratio >= 0.75 && matchCount > bestQAScore) {
      bestQAScore = matchCount;
      bestQA = item;
    }
  }

  if (bestQA) {
    return {
      isDirectQA: true,
      answer: bestQA.answer,
      page: bestQA.page,
      evidence: bestQA.evidence,
    };
  }

  // ----------------------------------------------------
  // TIER 2: Story Reading Prose Sliding Window Search
  // ----------------------------------------------------
  let bestChunk = null;
  let bestScore = 0;
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

      if (score > bestScore) {
        bestScore = score;
        bestChunk = chunk;
        bestPage = page.book_page;
      }
    }
  }

  if (bestScore >= 2 && bestChunk) {
    return {
      isDirectQA: false,
      chunk: bestChunk,
      page: bestPage,
    };
  }

  return null;
}
