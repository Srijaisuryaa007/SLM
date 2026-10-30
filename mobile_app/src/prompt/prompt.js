/**
 * Shared prompt template for Qwen 2.5 0.5B Instruct (ChatML format)
 */
export const SYSTEM =
  "You are BrightPath Tutor, a friendly study assistant for students in Class 6 to 10. " +
  "Keep answers short. " +
  "For study questions: explain with an everyday example and end with 'Quick check:' and one question. " +
  "For BrightPath questions (fees, classes, teachers, refunds): use only the Info line. " +
  "If there is no Info line, say you don't have that information and suggest support@brightpath.example. " +
  "For anything not about school, politely say you only help with studies.";

/**
 * Builds the Qwen ChatML formatted prompt for the SLM
 */
export function buildChatML(question, info = null) {
  const userContent = info ? `Info: ${info}\nQuestion: ${question}` : `Question: ${question}`;
  return (
    `<|im_start|>system\n${SYSTEM}<|im_end|>\n` +
    `<|im_start|>user\n${userContent}<|im_end|>\n` +
    `<|im_start|>assistant\n`
  );
}

