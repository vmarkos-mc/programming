# in-class/divisibility.py

m = int(input('Enter m: '))
n = int(input('Enter n: '))

# To check divisibility, we need to verify that the remainder of the
# division is actually zero.
if n % m == 0:
    print(f'{m} divides {n}.')
else:
    print(f'{m} does not divide {n}.')
