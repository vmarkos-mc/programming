# source/is_prime_008.py

from is_prime_005 import is_prime as ip

n = int(input("Please, enter an integer: "))
while n > 0:
    if ip(n):
        print("Prime!")
    else:
        print("Not Prime!")
    n = int(input("Please, enter an integer: "))