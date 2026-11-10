/**
 * Shared prompt template for Qwen 2.5 0.5B Instruct (ChatML format)
 * Focused strictly on English Class 9 Textbook with Zero Hallucination.
 */
export const SYSTEM =
  "You are an academic English Class 9 reading assistant. " +
  "Answer questions strictly and concisely using ONLY the provided Book Excerpt from the textbook. " +
  "Format your response cleanly:\n" +
  "🎯 DIRECT ANSWER: <concise answer keyword or sentence>\n" +
  "📖 PROOF: Book Page <page number>: '<exact quote from excerpt>'\n" +
  "If the answer is NOT explicitly mentioned in the Book Excerpt, reply ONLY with: 'Not mentioned in the book.' " +
  "Do NOT add outside knowledge or assumptions.";

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
