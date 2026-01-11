from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_pdf(summary_text, output_path="summary_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 40

    c.setFont("Helvetica", 11)

    for line in summary_text.split("\n"):
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 40

        c.drawString(x, y, line)
        y -= 14

    c.save()
