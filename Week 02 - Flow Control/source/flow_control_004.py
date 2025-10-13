# source/flow_control_004.py

n = int(input("Please, enter an integer: "))
if n < 8 and n < 4:
    output = "Okay"
elif n >= 4 and n < 8:
    output = "Yeah"
elif n < 9 or n < 16:
    output = "So..."
else:
    output = "But..."
print(output)