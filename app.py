import re
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        raise ValueError(r'''Provide a pdf file as an argument.
Example: python .\app.py "pdf_file.pdf"''')
    file: str = argv[1]
    if file.endswith(".pdf"):
        with open(file, "rb") as f:
            file_stream: bytes = f.read()
            file_stream = re.sub(rb"\n/Image.*", b"", file_stream)
        with open(file.strip(".pdf") + "_no_watermark.pdf", "wb") as f:
            f.write(file_stream)
    else:
        raise ValueError("Not a PDF file!")
