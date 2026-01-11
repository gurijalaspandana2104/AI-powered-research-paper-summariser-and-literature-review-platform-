import re
from pdf_parser import extract_text_from_pdf


def clean_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove references section
    text = re.split(r'References|REFERENCES', text)[0]

    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)

    # Remove special characters (keep basic punctuation)
    text = re.sub(r'[^a-zA-Z0-9.,;:()\-\s]', '', text)

    return text.strip()


def chunk_text(text, max_words=600):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


if __name__ == "__main__":
    raw_text = extract_text_from_pdf("papers/sample1.pdf")
    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text)

    print(f"TOTAL CHUNKS CREATED: {len(chunks)}\n")
    print("FIRST CHUNK:\n")
    print(chunks[0][:1000])
