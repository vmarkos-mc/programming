# source/is_prime_002.py

def is_prime(n):
    i = 2
    if n < 2:
        return False
    while n % i != 0:
        i = i + 1
    if n == i:
        return True
    return False