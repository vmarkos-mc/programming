# source/flow_control_003.py

grade = int(input("Please, enter your grade (0-100): "))
if grade >= 70:
    output = "Excellent"
elif grade < 70 and grade >= 40:
    output = "Pass"
else:
    output = "Fail"
print(output)