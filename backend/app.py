# from flask import Flask, render_template, request, send_file
# import os
# import fitz  # PyMuPDF
# from collections import Counter


# from pdf_parser import extract_text_from_pdf
# from text_cleaner import clean_text, chunk_text
# from summarizer import summarize_chunk
# from contributors_extractor import extract_contributors
# from section_formatter import format_literature_review
# from pdf_generator import generate_pdf

# app = Flask(__name__)

# UPLOAD_FOLDER = "papers"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# PDF_FILE = "final_summary.pdf"


# @app.route("/", methods=["GET", "POST"])
# def index():
#     summary = None
#     word_count = 0
#     page_count = 0
#     contributors = []

#     if request.method == "POST":
#         file = request.files.get("pdf")

#         if file and file.filename != "":
#             # 1️⃣ Save uploaded PDF
#             pdf_path = os.path.join(UPLOAD_FOLDER, "uploaded.pdf")
#             file.save(pdf_path)

#             # 2️⃣ Page count (CORRECT way)
#             doc = fitz.open(pdf_path)
#             page_count = len(doc)
#             doc.close()

#             # 3️⃣ Extract & clean text
#             raw_text = extract_text_from_pdf(pdf_path)
#             cleaned_text = clean_text(raw_text)

#             # 4️⃣ Word count
#             word_count = len(cleaned_text.split())

#             words = cleaned_text.lower().split()
#             filtered = [w for w in words if len(w) > 6 and w.isalpha()]
#             keywords = [w for w, _ in Counter(filtered).most_common(6)]


#             # 5️⃣ Extract contributors
#             contributors = extract_contributors(raw_text)

#             # 6️⃣ Chunk text
#             chunks = chunk_text(cleaned_text)

#             all_summaries = []

#             # 7️⃣ Summarize first 3 chunks
#             for i, chunk in enumerate(chunks[:3]):
#                 if len(chunk.strip()) < 50:
#                     continue
#                 print(f"Summarizing chunk {i+1}/{len(chunks)}")
#                 all_summaries.append(summarize_chunk(chunk))

#             # 8️⃣ Structured literature review
#             summary = format_literature_review(all_summaries, contributors)

#             # 9️⃣ Generate PDF
#             generate_pdf(summary, PDF_FILE)

#     return render_template(
#     "index.html",
#     summary=summary,
#     word_count=word_count,
#     page_count=page_count,
#     contributors=contributors,
#     keywords=keywords
# )


# @app.route("/download")
# def download():
#     return send_file(PDF_FILE, as_attachment=True)


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, send_file
import os
import fitz  # PyMuPDF
from collections import Counter

from pdf_parser import extract_text_from_pdf
from text_cleaner import clean_text, chunk_text
from summarizer import summarize_chunk
from contributors_extractor import extract_contributors
from section_formatter import format_literature_review
from pdf_generator import generate_pdf
from chatbot import chat_reply   # 🔹 CHATBOT IMPORT

app = Flask(__name__)

UPLOAD_FOLDER = "papers"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

PDF_FILE = "final_summary.pdf"

# 🔹 GLOBAL CACHE FOR CHATBOT CONTEXT
cached_paper_text = ""


@app.route("/", methods=["GET", "POST"])
def index():
    global cached_paper_text

    summary = None
    word_count = 0
    page_count = 0
    contributors = []
    keywords = []

    if request.method == "POST":
        file = request.files.get("pdf")

        if file and file.filename != "":
            # 1️⃣ Save uploaded PDF
            pdf_path = os.path.join(UPLOAD_FOLDER, "uploaded.pdf")
            file.save(pdf_path)

            # 2️⃣ Page count
            doc = fitz.open(pdf_path)
            page_count = len(doc)
            doc.close()

            # 3️⃣ Extract & clean text
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned_text = clean_text(raw_text)

            # 🔹 Cache text for chatbot
            cached_paper_text = cleaned_text

            # 4️⃣ Word count
            word_count = len(cleaned_text.split())

            # 5️⃣ Keyword extraction (SAFE, NO AI)
            words = cleaned_text.lower().split()
            filtered = [w for w in words if len(w) > 6 and w.isalpha()]
            keywords = [w for w, _ in Counter(filtered).most_common(6)]

            # 6️⃣ Contributors
            contributors = extract_contributors(raw_text)

            # 7️⃣ Chunk text
            chunks = chunk_text(cleaned_text)

            # 8️⃣ Summarize first 3 chunks (performance-safe)
            all_summaries = []
            for i, chunk in enumerate(chunks[:3]):
                if len(chunk.strip()) < 50:
                    continue
                print(f"Summarizing chunk {i+1}/{len(chunks)}")
                all_summaries.append(summarize_chunk(chunk))

            # 9️⃣ Structured literature review
            summary = format_literature_review(all_summaries, contributors)

            # 🔟 Generate PDF
            generate_pdf(summary, PDF_FILE)

    return render_template(
        "index.html",
        summary=summary,
        word_count=word_count,
        page_count=page_count,
        contributors=contributors,
        keywords=keywords
    )


# 🔹 CHATBOT ENDPOINT
@app.route("/chat", methods=["POST"])
def chat():
    global cached_paper_text

    data = request.json
    user_msg = data.get("message", "").strip()

    if not user_msg:
        return {"reply": "Please ask a valid question."}

    if not cached_paper_text:
        return {"reply": "Please upload a research paper first."}

    reply = chat_reply(user_msg, cached_paper_text)
    return {"reply": reply}


@app.route("/download")
def download():
    return send_file(PDF_FILE, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
