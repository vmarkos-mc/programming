# source/is_prime_004.py

import is_prime_003

n = int(input("Please, enter an integer: "))
while n > 0:
    if is_prime_003.is_prime(n):
        print("Prime!")
    else:
        print("Not Prime!")
    n = int(input("Please, enter an integer: "))