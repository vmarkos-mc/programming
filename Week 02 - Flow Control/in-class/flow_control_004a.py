# in-class/flow_control_004a.py

# source/flow_control_004.py

n = int(input("Please, enter an integer: "))
if n < 4:
    output = "Okay"
elif n < 8:
    output = "Yeah"
elif n < 16:
    output = "So..."
else:
    output = "But..."
print(output)