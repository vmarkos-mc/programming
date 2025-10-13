# source/flow_control_003a.py

grade = int(input("Please, enter your grade (0-100): "))
if grade >= 70:
    output = "Excellent"
elif grade >= 40:
    output = "Pass"
else:
    output = "Fail"
print(output)