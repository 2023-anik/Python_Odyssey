from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"

pdf_reader = PdfReader(pdf_path)

pdf_writer = PdfWriter()

# Append the first page of the input PDF to the output PDF
