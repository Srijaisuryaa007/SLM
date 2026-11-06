"""The ONE place that decides what the model reads.
Configured for English Class 9 Textbook Reading Assistant.
"""

SYSTEM = (
    "You are an academic English Class 9 reading assistant. "
    "Answer questions strictly and concisely using ONLY the provided Book Excerpt from the textbook. "
    "Keep answers to 1-2 direct sentences. "
    "If the answer is NOT explicitly mentioned in the Book Excerpt, reply ONLY with: 'Not mentioned in the book.' "
    "Do NOT add outside knowledge or assumptions."
)


def make_message(question, info=None, page_no=None):
    """What the student's turn looks like. 'info' is the matching book excerpt."""
    if info:
        page_str = f" (Book Page {page_no})" if page_no else ""
        return f"Book Excerpt{page_str}:\n\"{info}\"\n\nQuestion: {question}"
    return f"Question: {question}"
