# source/is_prime_006.py

import is_prime_005

n = int(input("Please, enter an integer: "))
while n > 0:
    if is_prime_005.is_prime(n):
        print("Prime!")
    else:
        print("Not Prime!")
    n = int(input("Please, enter an integer: "))