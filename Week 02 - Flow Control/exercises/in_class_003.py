# in-class/in_class_003.py

import math

a = float(input("Please, enter 'a' (a != 0): "))
while a == 0:
    a = float(input("Please, enter 'a' (a != 0): "))
b = float(input("Please, enter 'b': "))
c = float(input("Please, enter 'c': "))

# Discriminant
d = b ** 2 - 4 * a * c

if d == 0:
    x = -b / (2 * a) # WRONG!!! -b / 2 * a first divides, then multiplies
    print(f"Single solution: {x}")
elif d > 0:
    x_1 = (-b + d ** 0.5) / (2 * a) # One way is to recall that sqrt(x) == x ^ (1/2).
    x_2 = (-b - math.sqrt(d)) / (2 * a) # Another is to use `math.sqrt()`.
    print(f"Two solutions: {x_1}, {x_2}")
else:
    print("No real roots!")