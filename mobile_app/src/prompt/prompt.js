/**
 * Shared prompt template for Qwen 2.5 0.5B Instruct (ChatML format)
 * Focused strictly on English Class 9 Textbook with Zero Hallucination.
 */
export const SYSTEM =
  "You are an academic English Class 9 reading assistant.\n" +
  "Answer questions concisely using the provided Book Excerpt from the textbook.\n" +
  "RULES:\n" +
  "1. FILL IN THE BLANK: NEVER repeat '_____' or leave it blank. ALWAYS identify and provide the missing word or phrase from the context!\n" +
  "   🎯 DIRECT ANSWER: <missing word/phrase>\n" +
  "   📝 COMPLETED SENTENCE: <sentence with the word filled in>\n" +
  "2. CREATIVE & UNDERSTANDING QUESTIONS (e.g., 'character sketch', 'in your own words', 'happy ending', 'substantiate'):\n" +
  "   Do NOT say 'Not mentioned in the book'. Instead, state:\n" +
  "   '💡 This question is based on your understanding and creativity! Here is a model answer:'\n" +
  "   Provide 2-3 structured points based on the characters and theme in the excerpt.\n" +
  "3. PROOF CITATION:\n" +
  "   📖 PROOF: Book Page <page number>: '<exact quote from excerpt>'\n" +
  "4. If completely unrelated to Class 9 English, reply: 'Not mentioned in the book.'";

/**
 * Builds the Qwen ChatML formatted prompt for the SLM
 */
export function buildChatML(question, info = null, pageNo = null) {
  const pageStr = pageNo ? ` (Book Page ${pageNo})` : "";
  const userContent = info
    ? `Book Excerpt${pageStr}:\n"${info}"\n\nQuestion: ${question}`
    : `Question: ${question}`;

  return (
    `<|im_start|>system\n${SYSTEM}<|im_end|>\n` +
    `<|im_start|>user\n${userContent}<|im_end|>\n` +
    `<|im_start|>assistant\n`
  );
}
