# source/unique_002.py

def read_ints():
    numbers = set() # Initialise an empty set
    n = int(input("Please, enter an integer: "))
    while n > 0:
        numbers.add(n) # .add() is like .append() for lists
        n = int(input("Please, enter an integer: "))
    return numbers

if __name__ == "__main__":
    ns = read_ints()
    print(ns)