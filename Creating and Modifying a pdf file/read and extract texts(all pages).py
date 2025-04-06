from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"
# print(pdf_path.exists())

pdf_reader = PdfReader(pdf_path)

# print(len(pdf_reader.pages)) # to get the number of pages
# print(pdf_reader.metadata) # to get the document's information
# print(pdf_reader.metadata.title) # to get the document's title
# print(pdf_reader.metadata.author) # to get the document's author
# print(pdf_reader.metadata.subject) # to get the document's subject
# print(pdf_reader.metadata.producer) # to get the document's producer
# print(pdf_reader.metadata.creator) # to get the document's creator


# for page in pdf_reader.pages:
#     text = page.extract_text() # to extract text from the page
#     print(text)


output_file_path = Path.home() / "Pride_and_Prejudice.txt"

with output_file_path.open("w") as output_file:
    output_file.write(
        f"{pdf_reader.metadata.title}\n"
        f"Number of pages: {len(pdf_reader.pages)}\n"
    )
    for page in pdf_reader.pages:
        text = page.extract_text()  # to extract text from the page
        output_file.write(text)