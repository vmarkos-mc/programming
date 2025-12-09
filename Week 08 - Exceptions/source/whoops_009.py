# source/whoops_009.py

if __name__ == "__main__":
    try:
        x = float(input("Enter a float to compute its inverse: "))
        inv = 1 / x
    except ZeroDivisionError:
        print("Zero has no inverse!")
    else:
        print(f"1 / {x} == {inv}")