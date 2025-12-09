# source/files_003.py

import os
import csv

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(CWD, "students.csv")
    students = dict() # Initialise an empty dictionary
    with open(PATH, "r") as file: # Open the file
        reader = csv.reader(file) # Create a csv reader
        for row in reader: # Iterate over the file's lines
            # data is a list containing: [name, age, grade] as *strings*
            if row[0] != "Name": # In case we read the first line, we just ignore it
                students[row[0]] = (row[1], row[2])
    print(students)