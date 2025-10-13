# source/unique_001.py

def read_ints():
    numbers = []
    n = int(input("Please, enter an integer: "))
    while n > 0:
        numbers.append(n)
        n = int(input("Please, enter an integer: "))
    return numbers

def get_unique(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    return unique

if __name__ == "__main__":
    ns = read_ints()
    unique = get_unique(ns)
    print(unique)