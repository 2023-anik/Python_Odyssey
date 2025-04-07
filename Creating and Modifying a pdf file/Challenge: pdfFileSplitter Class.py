from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

class pdfFileSplitter:
    def __init__(self, pdf_path):
        self.pdf_reader = PdfReader(pdf_path)
        self.writer1 = None
        self.writer2 = None
    
    def split_pdf(self, breakpoint):
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()

        # Split the PDF into two parts
        # for n in range(0,breakpoint):
        #     page = self.pdf_reader.pages[n]
        #     self.writer1.add_page(page)
        
        # for n in range(breakpoint, len(self.pdf_reader.pages)):
        #     page = self.pdf_reader.pages[n]
        #     self.writer2.add_page(page)
        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.add_page(page)
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.add_page(page)
        
    def write_pdf(self, new_filename):
        with Path(Path.home() / f"{new_filename}_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)
        
        with Path(Path.home() / f"{new_filename}_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)

# Example usage
pdf_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"
# print(pdf_path.exists())

pdf_splitter = pdfFileSplitter(pdf_path)
pdf_splitter.split_pdf(breakpoint=150)
pdf_splitter.write_pdf("Pride_and_Prejudice_Split")