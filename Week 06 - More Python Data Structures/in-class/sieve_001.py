# in-class/sieve_001.py

from math import sqrt
from timeit import timeit

def primes(n):
    '''Accepts a (positive) integer n and returns a list of all primes
    up to n using Eratosthene's Sieve.'''

    if n < 2: # Dummy case
        return []
    # Create a list of numbers from 2 up to n.
    numbers = list(range(2, n + 1))
    prime_numbers = [] # Here we keep all primes found
    next_prime = numbers.pop(0)
    prime_numbers.append(next_prime)
    while next_prime <= sqrt(n):
        # First, we remove all multiples of `next_prime`
        temp_numbers = []
        for x in numbers:
            if x % next_prime != 0:
                temp_numbers.append(x)
        numbers = temp_numbers
        next_prime = numbers.pop(0)
        prime_numbers.append(next_prime)
    # All numbers that survive the above process are primes
    prime_numbers += numbers
    return prime_numbers


def primes_01(n):
    '''Accepts a (positive) integer n and returns a list of all primes
    up to n using Eratosthene's Sieve.'''

    if n < 2: # Dummy case
        return []
    # Create a list of numbers from 2 up to n.
    if n % 2 == 0:
        numbers = list(range(n-1, 1, -2))
    else:
        numbers = list(range(n, 1, -2))
    prime_numbers = [2] # Here we keep all primes found
    next_prime = numbers.pop()
    prime_numbers.append(next_prime)
    while next_prime <= sqrt(n):
        # First, we remove all multiples of `next_prime`
        temp_numbers = []
        for x in numbers:
            if x % next_prime != 0:
                temp_numbers.append(x)
        numbers = temp_numbers
        next_prime = numbers.pop()
        prime_numbers.append(next_prime)
    # All numbers that survive the above process are primes
    prime_numbers += numbers
    return prime_numbers


if __name__ == '__main__':
    N = 10000
    n = int(input('Please, enter n: '))
    prime_times_00 = timeit(lambda : primes(n), number=N)
    prime_times_01 = timeit(lambda : primes_01(n), number=N)
    print(
        f'Avg exec time: {prime_times_00}\n'
        f'Avg exec time: {prime_times_01}'
    )