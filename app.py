import re
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        raise ValueError(r'''Provide a pdf file as an argument.
Example: python .\app.py "pdf_file.pdf"''')
    file: str = argv[1]
    if not file.endswith(".pdf"):
        raise ValueError("Not a PDF file!")
    with open(file, "rb") as f:
        file_stream: bytes = f.read()
        file_stream = re.sub(rb"\n/Image.*", b"", file_stream)
    with open(file.strip(".pdf") + "_watermarkless.pdf", "wb") as f:
        f.write(file_stream)
    print("Done!")
