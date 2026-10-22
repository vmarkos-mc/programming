# in-class/ex_003.py

from math import sqrt

# Read user input
a = float(input('Enter a (a != 0): '))
while a == 0.0:
    a = float(input('Enter a (a != 0): '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# Compute the discriminant
d = b ** 2 - 4 * a * c

if d < 0:
    print('No real roots!')
elif d == 0.0:
    x = -b / (2 * a)
    print(f'Double real root: {x}.')
else:
    # x1 = (-b + d ** 0.5) / (2 * a)
    x1 = (-b + sqrt(d)) / (2 * a)
    # x2 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'Two real roots: {x1}, {x2}.')