# source/flow_control_020.py

n = int(input("Enter an integer: "))
s = 0
while n != 0:
    if n % 2 == 0:
        s = s + n
    n = int(input("Enter an integer: "))
print("Sum of even numbers: ", s)