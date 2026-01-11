import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


if __name__ == "__main__":
    pdf_path = "papers/sample1.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)

    print("TEXT EXTRACTED SUCCESSFULLY")
    print(extracted_text[:1000])  # first 1000 characters
