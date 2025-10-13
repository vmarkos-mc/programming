# source/foo_001.py

def foo(x):
    x = x + 4
    return x

if __name__ == "__main__":
    x = 6
    y = foo(x)
    print(f"x: {x}, y: {y}.")
