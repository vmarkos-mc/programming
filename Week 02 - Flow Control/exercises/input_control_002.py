# in-class/input_control_002.py

grade = int(input("Grade: "))
if grade < 0 or grade > 100:
    grade = int(input("Please enter a value between 0 and 100: "))
if grade >= 70:
    print("Pass!")
else:
    print("Fail!")