// Pure JavaScript RAG search matching ask.py
import facts from '../../assets/facts.json';

const STOP = new Set(
  "a an the is are was of for to in on at and or do does i my me you your what whats how can when who which there it be with about tell please much many have has will if any get this that fee"
    .split(" ")
);

function getWords(text) {
  const matches = text.toLowerCase().match(/[a-z0-9]+/g) || [];
  return matches.filter((w) => !STOP.has(w));
}

/**
 * Searches the local facts.json on-device and returns the best matching fact text, or null.
 */
export function findFact(question) {
  const qWords = getWords(question);
  const numbers = qWords.filter((w) => /^\d+$/.test(w));

  let bestFact = null;
  let bestScore = 0;

  for (const fact of facts) {
    const fWords = new Set(getWords(fact.text));

    // If question specifies a number (like "Class 9"), the fact must have that number
    const hasAllNumbers = numbers.every((n) => fWords.has(n));
    if (!hasAllNumbers) continue;

    let score = 0;
    for (const w of qWords) {
      if (fWords.has(w)) score++;
    }

    if (score > bestScore) {
      bestScore = score;
      bestFact = fact;
    }
  }

  return bestFact ? bestFact.text : null;
}

