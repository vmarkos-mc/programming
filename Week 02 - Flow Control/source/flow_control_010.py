# source/flow_control_010.py

grade = int(input("Please, enter your grade: "))
if grade >= 90:
    af_grade = "A"
elif grade >= 80:
    af_grade = "B"
elif grade >= 70:
    af_grade = "C"
elif grade >= 60:
    af_grade = "D"
else:
    af_grade = "F"
print(af_grade)