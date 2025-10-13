# source/flow_control_008.py

year = int(input("Please, enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year!")
else:
    print("Not leap year!")