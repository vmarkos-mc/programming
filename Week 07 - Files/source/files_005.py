# source/files_005.py

import os
import csv
import json

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    rows = [
        ["Name", "Age", "Grade"],
        ["Alice", "12", "A"],
        ["Bob", "10", "B"],
        ["Charlie", "14", "C"],
    ]
    CSV_PATH = os.path.join(CWD, "students_w.csv")
    with open(CSV_PATH, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rows)