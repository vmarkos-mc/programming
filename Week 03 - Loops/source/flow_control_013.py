# source/flow_control_013.py

grade = int(input("Please, enter your grade (0-100): "))
if grade > 100 or grade < 0:
    grade = int(input("Please, enter your grade (0-100): "))
if grade > 100 or grade < 0:
    grade = int(input("Please, enter your grade (0-100): "))
if grade >= 70:
    output = "Pass"
else:
    output = "Fail"
print(output)