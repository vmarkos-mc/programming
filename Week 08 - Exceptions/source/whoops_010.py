# source/whoops_010.py

def foo():
    try:
        raise KeyboardInterrupt
    finally:
        print("Oh, noooo!")

if __name__ == "__main__":
    foo()