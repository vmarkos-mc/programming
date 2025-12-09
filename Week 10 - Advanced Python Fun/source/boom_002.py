# source/boom_002.py

def bar(a, b, *args):
    if not args:
        return a + b
    return sum(args)

if __name__ == "__main__":
    print(bar(1, 2))
    print(bar(1, 3, 2))
    print(bar(1))
    print("What?")