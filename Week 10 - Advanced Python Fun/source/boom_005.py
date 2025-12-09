# source/boom_005.py

def add(a, b, c):
    return a + b + c

if __name__ == "__main__":
    xs = {'a': 4, 'b': 6, 'c': 2}
    print(add(a=xs['a'], b=xs['b'], c=xs['c'])) # Old-school
    print(add(**xs)) # Pythonic