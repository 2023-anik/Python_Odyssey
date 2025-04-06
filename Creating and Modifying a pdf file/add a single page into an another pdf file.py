from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(pdf_path)
first_page = input_pdf.pages[0]

pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)

with Path(Path.home()/"first_page.pdf").open("wb") as output_pdf:
    pdf_writer.write(output_pdf)