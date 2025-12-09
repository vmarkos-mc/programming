# source/flow_control_009.py

year = int(input("Please, enter a year: "))
if year % 400 == 0:
    print("Leap year!")
elif year % 100 == 0:
    print("Not leap year!")
elif year % 4 == 0:
    print("Leap year!")
else:
    print("Not leap year!")

"""
if year % 4 == 0 or year % 400 == 0:
    print("leap")
elif year % 100 != 0:
    print("not leap")
"""