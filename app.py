from sys import argv

import fitz

if __name__ == "__main__":
    file: str = argv[1]
    if file.endswith(".pdf"):
        doc = fitz.open(file)
        for xref in range(1, doc.xref_length()):
            if stream := doc.xref_stream(xref):
                stream = stream.replace(b"Image", b"")
                doc.update_stream(xref, stream)
        doc.save(file.strip(".pdf") + "_no_watermark.pdf")
    else:
        raise ValueError("Not a PDF file!")
