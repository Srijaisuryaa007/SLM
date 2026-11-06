// On-device RAG search matching ask.py
import bookPages from '../../assets/facts.json';

const STOP = new Set(
  "a an the is are was were of for to in on at and or do does did i my me you your what whats how can could when who whom which where there it be been with about tell please much many have has had will would if any get this that these those from by"
    .split(" ")
);

function getWords(text) {
  const matches = text.toLowerCase().match(/[a-z0-9]+/g) || [];
  return matches.filter((w) => !STOP.has(w));
}

/**
 * Searches the local English Class 9 textbook on-device and returns the best matching excerpt, or null.
 */
export function findFact(question) {
  const qWords = getWords(question);
  if (qWords.length === 0) return null;

  let bestChunk = null;
  let bestScore = 0;

  for (const page of bookPages) {
    if (!page.text) continue;
    // Split into sentences
    const sentences = page.text.split(/(?<=[.!?])\s+/);
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
      }
    }
  }

  return bestChunk;
}
