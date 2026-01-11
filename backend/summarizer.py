# from transformers import pipeline
# from text_cleaner import clean_text, chunk_text
# from pdf_parser import extract_text_from_pdf


# def summarize_chunk(text):
#     summarizer = pipeline(
#         "summarization",
          
#  model="sshleifer/distilbart-cnn-6-6"

#     )

#     summary = summarizer(
#         text,
#         max_length=150,
#         min_length=60,
#         do_sample=False
#     )

#     return summary[0]["summary_text"]


# if __name__ == "__main__":
#     raw_text = extract_text_from_pdf("papers/sample1.pdf")
#     cleaned_text = clean_text(raw_text)

#     chunks = chunk_text(cleaned_text)

#     print("Summarizing first chunk...\n")
#     summary = summarize_chunk(chunks[0])

#     print("SUMMARY:\n")
#     print(summary)


# def summarize_all_chunks(chunks):
#     summaries = []

#     for i, chunk in enumerate(chunks):
#         print(f"Summarizing chunk {i+1}/{len(chunks)}...")
#         summary = summarize_chunk(chunk)
#         summaries.append(summary)

#     return summaries
from transformers import pipeline

# ✅ Load model ONCE (global)
summarizer_pipeline = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6",
    device=-1  # CPU only
)

def summarize_chunk(text):
    # 🔒 SAFETY TRUNCATION (VERY IMPORTANT)
    max_chars = 3000
    text = text[:max_chars]

    summary = summarizer_pipeline(
        text,
        max_length=150,
        min_length=60,
        do_sample=False
    )

    return summary[0]["summary_text"]


def summarize_all_chunks(chunks):
    summaries = []

    for i, chunk in enumerate(chunks):
        if len(chunk.strip()) < 50:
            continue

        print(f"Summarizing chunk {i+1}/{len(chunks)}...")
        summaries.append(summarize_chunk(chunk))

    return summaries
