# source/files_006.py

import os
import csv
import json

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(CWD, "students.txt")
    students = dict() # Initialise an empty dictionary
    with open(PATH, "r") as file: # Open the file
        reader = csv.reader(file) # Create a csv reader
        for row in reader: # Iterate over the file's lines
            # data is a list containing: [name, age, grade] as *strings*
            if row[0] != "Name": # In case we read the first line, we just ignore it
                students[row[0]] = (row[1], row[2])
    JSON_PATH = os.path.join(CWD, "students_w.json")
    with open(JSON_PATH, "w") as file:
        json.dump(students, file, indent=2)