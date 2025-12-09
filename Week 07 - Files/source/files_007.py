# source/files_007.py

import os

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(CWD, "a_file.txt")
    rows = [
        "This is a file.",
        "Actually, this is not just a file",
        "As you might well see on your own...",
        "...this is a...",
    ]
    with open(PATH, "w") as file:
        for row in rows:
            file.write(row)
            file.write("\n")