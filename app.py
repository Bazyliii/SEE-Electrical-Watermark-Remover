from sys import argv
from pathlib import Path
import re

if __name__ == "__main__":
    if len(argv) != 2:
        raise ValueError(r'''Provide a pdf file as an argument.
Example: python .\app.py "pdf_file.pdf"''')
    file: Path = Path(argv[1])
    if not file.suffix == ".pdf":
        raise ValueError("Not a PDF file!")
    with file.open("rb") as f:
        file_stream = f.read()
        # with file.with_name(file.stem + "_stream.txt").open("w") as f:
        #     f.write(str(file_stream))
        pattern_string = ""
        for i in range(98, 158, 1):
            pattern_string += r"\n/Image\d{1,}\s" + str(i) + r"\s0\sR|"
        for i in range(211, 238, 1):
            pattern_string += r"\n/Image\d{1,}\s" + str(i) + r"\s0\sR|"
        pattern_string = pattern_string[:-1]
        remove_pattern = re.compile(pattern_string.encode("utf-8"))
        file_stream = re.sub(remove_pattern, b"", file_stream)

    with file.with_name(file.stem + "_watermarkless" + file.suffix).open("wb") as f:
        f.write(file_stream)
    print("Done!")
