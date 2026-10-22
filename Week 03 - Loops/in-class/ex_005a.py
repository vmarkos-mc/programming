# in-class/ex_005.py

from math import sqrt

# Ask for user input
n = int(input('Enter n: '))
while n <= 0:
    n = int(input('Enter n: '))

i = 1 # Counter, looking for divisors
while i <= sqrt(n):
    # If i divides n...
    if n % i == 0:
        # print `i`
        j = n // i # Integer division
        print(f'({i}, {j})', end=' ')
    i = i + 1 # i += 1

# Key observation:
# Consider the divisors of 24:
# 24: 1, 2, 3, 4, 6, 8, 12, 24
# 24 = 1 * 24
# 24 = 2 * 12
# 24 = 3 * 8
# 24 = 4 * 6 <-- We need not check beyond this point.
# 24 = 6 * 4
# 24 = 8 * 3
# 24 = 12 * 2
# 24 = 24 * 1
#
# What is this "this point" above?. It is the point in which in the expression
# 24 = i * j, i < j and then, for the same expression, we have: i > j.
# Equivalently, we need to check for values of i such that, in the edge case:
# 24 = i * j, where i <= j, so, in the limit: i == j, i.e., 24 = i * i = i ** 2,
# So we need not check beyond sqrt(24)
# In general, when looking for divisors, we need not look beyond sqrt(n).