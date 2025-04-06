from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"

pdf_reader = PdfReader(pdf_path)

pdf_writer = PdfWriter()

for n in range(1, 4):
    page = pdf_reader.pages[n]
    pdf_writer.add_page(page)

with Path(Path.home()/"multiple_pages.pdf").open("wb") as output_pdf:
    pdf_writer.write(output_pdf)