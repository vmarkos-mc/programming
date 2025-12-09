# source/files_002.py

import os

if __name__ == "__main__":
    CWD = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(CWD, "students.txt")
    file = open(PATH, "r") # Open the file
    students = dict() # Initialise an empty dictionary
    for line in file.readlines(): # Iterate over the file's lines
        data = line.split(",")
        # data is a list containing: [name, age, grade] as *strings*
        if data[0] != "Name": # In case we read the first line, we just ignore it
            students[data[0]] = (data[1], data[2].strip())
        # Why do we use .strip()?
    file.close()
    print(students)