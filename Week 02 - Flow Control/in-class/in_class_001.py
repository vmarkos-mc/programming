# in-class/in_class_001.py

n = int(input("Please enter the number of tutorials: "))
# n_str = input("...")
# n = int(n_str)

if n <= 5:
    # First 5 tutorials are free.
    cost = 0
elif n <= 15:
    # Next 10 come at 5$ each.
    cost = (n - 5) * 5
elif n <= 35:
    # Next 20 come at 4$ each.
    cost = (n - 15) * 4 + 10 * 5
else:
    # Any more come at 2.5$ each.
    cost = 10 * 5 + 20 * 4 + (n - 35) * 2.5
print(f"Total cost: {cost}.")