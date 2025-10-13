# source/flow_control_018.py

s = 0 # We initialise the target sum at 0.
c = 0 # The count of user-provided numbers
n = int(input("Enter an integer: "))
while n > 0:
    s = s + n
    c = c + 1
    n = int(input("Enter an integer: "))
avg = s / c
print("The average is:", avg)