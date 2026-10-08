# in-class/divisibility_002.py

m = int(input('Enter m: '))
n = int(input('Enter n: '))

# Alternative:
# if n % m == 0 and not m % m**2 == 0:
if n % m == 0 and m % m**2 != 0:
    print('Simple divisor!')
else:
    print('Non-simple divisor!')