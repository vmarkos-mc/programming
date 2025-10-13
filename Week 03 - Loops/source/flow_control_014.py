# source/flow_control_014.py

grade = int(input("Please, enter your grade (0-100): "))
while grade > 100 or grade < 0:
    grade = int(input("Please, enter your grade (0-100): "))

if grade >= 70:
    output = "Pass"
else:
    output = "Fail"
print(output)