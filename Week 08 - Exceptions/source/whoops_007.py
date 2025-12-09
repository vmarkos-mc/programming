# source/whoops_007.py

import random

if __name__ == "__main__":
    fancy_numbers = { i: random.choice([True, False]) for i in range(100)}
    try:
        n = int(input("Enter an integer: "))
        print(f"Is {n} fancy?: {fancy_numbers[n]}.")
    except ValueError:
        print(f"You messed up!")
    except KeyError:
        print(f"{n} is not eligible for fanciness.")