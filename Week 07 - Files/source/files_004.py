# source/files_004.py

import os
import json

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(CWD, "students.json")
    with open(PATH, "r") as file: # Open the file
        students = json.load(file) # Create a csv reader
    print(students)