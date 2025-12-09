# source/boom_004.py

def add(a, b, c):
    return a + b + c

if __name__ == "__main__":
    xs = [3, 1, 2]
    print(add(xs[0], xs[1], xs[2])) # Old-school
    print(add(*xs)) # Pythonic