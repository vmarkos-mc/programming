# source/files_001.py

if __name__ == "__main__":
    file = open("students.txt", "r") # Open the file
    students = dict() # Initialise an empty dictionary
    for line in file.readlines(): # Iterate over the file's lines
        data = line.split(",")
        # data is a list containing: [name, age, grade] as *strings*
        if data[0] != "Name": # In case we read the first line, we just ignore it
            students[data[0]] = (data[1], data[2].strip())
        # Why do we use .strip()?
    file.close()
    print(students)