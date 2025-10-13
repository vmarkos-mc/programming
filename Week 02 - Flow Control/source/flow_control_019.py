# source/flow_control_019.py

n = int(input("Enter an integer: "))
s = 0
while n != 0:
    n = int(input("Enter an integer: "))
    if n % 2 == 0:
        s = s + n
print("Sum of even numbers: ", s)