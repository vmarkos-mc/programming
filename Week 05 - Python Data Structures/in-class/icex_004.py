# in-class/icex_004.py

from math import sqrt

def compute_sd_failed():
    s = 0 # Compute the sum, useful for the mean value
    n = 0 # Also, keep track of count
    x = float(input('Please, enter a number: '))
    while x != 0:
        n += 1
        s += x
        x = float(input('Please, enter a number: '))
    if n == 0: # Edge case: no non-zero number provided
        return 0.0
    mean = s / n
    # Now, what? We should have used a list to keep track of x values!
    ...


def compute_sd():
    s = 0 # Compute the sum, useful for the mean value
    n = 0 # Also, keep track of count
    numbers = list()
    x = float(input('Please, enter a number: '))
    while x != 0:
        numbers.append(x)
        n += 1
        s += x
        x = float(input('Please, enter a number: '))
    if n == 0: # Edge case: no non-zero number provided
        return 0.0
    mean = s / n
    # We can now loop through those numbers again:
    sd = 0
    for x in numbers:
        sd += (x - mean) ** 2
    return sqrt(sd / n)


def main():
    sd = compute_sd()
    print(sd)


if __name__ == '__main__':
    main()