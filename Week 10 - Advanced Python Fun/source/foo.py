# source/foo.py

def foo(*args):
    if not args:
        print("Opps! No arguments!")
        return
    for i, arg in enumerate(args):
        print(f"{i}: {arg}", end=" ")
    print()