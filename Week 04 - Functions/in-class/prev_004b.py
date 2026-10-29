# in-class/prev_004b.py

from math import sqrt, ceil

# A note on rounding:
#   * math.ceil() rounds towards infinities.
#   * math.floor() rounds towards 0.
#   * math.round() rounds towards at 0.5, i.e., 6.5 --> 7, 6.43 --> 6.

n = int(input('Please, enter an integer: '))

is_prime = True # This is a so-called "flag" variable
if n > 1:
    m = ceil(sqrt(n)) + 1
    for i in range(2, m): # Since 1 and n always divide n
        if n % i == 0 and i != n:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f'{n} is prime!')
else:
    print(f'{n} is not prime!')


# `while` alternative
# if n > 1:
#     i = 2
#     while n % i != 0:
#         i = i + 1
#     if i == n:
#         print(f'{n} is prime!')
#     else:
#         print(f'{n} is not prime!')
# else:
#     print(f'{n} is not a prime!')