# source/is_prime_001.py

def is_prime(n):
    i = 2
    if n < 2:
        return False
    else:
        while n % i != 0:
            i = i + 1
        if n == i:
            return True
        else:
            return False