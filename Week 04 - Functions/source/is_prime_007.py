# source/is_prime_007.py

from is_prime_005 import is_prime

n = int(input("Please, enter an integer: "))
while n > 0:
    if is_prime(n):
        print("Prime!")
    else:
        print("Not Prime!")
    n = int(input("Please, enter an integer: "))