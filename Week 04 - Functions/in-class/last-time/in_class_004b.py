# last-time/in_class_004b.py

from math import sqrt, ceil # sqrt --> square root, ceil --> round towards +infinity

n = int(input("Please, enter an integer: "))

# This is a boolean flag, which is True when n is prime and False otherwise
# We initialise to True since the only case in which is_prime changes its value
# is when we encounter a nonb-trivial divisor, in which case we set it to 
# False.
# So, by default, we assume that n is a prime and try to refute it.
is_prime = True

if n > 1:
    # We need not check for i == 1 or i == n.
    # for i in range(2, n): # First approach, the slowest one
    # for i in range(2, n // 2 + 1): # Second, faster approach
    for i in range(2, ceil(sqrt(n)) + 1): # This is just for n == 4
        # If we find a non-trivial divisor of n, break
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is prime!")
    else:
        print(f"{n} is not prime!")
else:
    print(f"{n} is not prime!")