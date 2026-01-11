from transformers import pipeline

# Lightweight QA-style pipeline
chat_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",   # small, conversational, fast
    device=-1
)

def chat_reply(question, paper_text):
    """
    Generate conversational answer using paper context.
    """

    prompt = f"""
    You are a helpful research assistant.
    Answer the user's question in simple words.

    Paper context:
    {paper_text[:2000]}

    Question:
    {question}

    Answer:
    """

    response = chat_model(
        prompt,
        max_length=120,
        do_sample=False
    )

    return response[0]["generated_text"].strip()
