# source/flow_control_017.py

s = 0 # We initialise the target sum at 0.
n = int(input("Enter an integer: "))
while n > 0:
    s = s + n
    n = int(input("Enter an integer: "))
print("The sum is:", s)