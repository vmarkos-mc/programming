# source/flow_control_011.py

income = float(input("Your income: "))
if income <= 10000:
    tax = 0
elif income <= 15000:
    tax = (income - 10000) * 0.05
elif income <= 30000:
    tax = 5000 * 0.05 + (income - 15000) * 0.20
else:
    tax = 5000 * 0.05 + 15000 * 0.20 + (income - 30000) * 0.40
print("Tax due:", tax)