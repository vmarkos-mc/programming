# source/is_prime_005.py

def is_prime(n):
    i = 2
    if n < 2:
        return False
    while n % i != 0:
        i = i + 1
    if n == i:
        return True
    return False

if __name__ == "__main__":
    n = int(input("Please, enter an integer: "))
    while n > 0:
        if is_prime(n):
            print("Prime!")
        else:
            print("Not Prime!")
        n = int(input("Please, enter an integer: "))