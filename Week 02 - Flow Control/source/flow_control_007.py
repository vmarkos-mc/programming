# source/flow_control_007.py
n = int(input("Please, enter an integer: "))
if n % 2 == 0:
    output = "Fly!"
elif n % 6 == 0:
    output = "Fry!"
elif n % 3 == 0:
    output = "Cry!"
else:
    output = "Bye!"
print(output)