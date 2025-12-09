# source/whoops_003.py

if __name__ == "__main__":
    try:
        a = float(input("Enter a: "))
    except ValueError:
        a = float(input("Please, enter a float for a: "))
    b = float(input("Enter b: "))
    while b == 0:
        b = float(input("Invalid value, b == 0! Enter b: "))
    c = a / b
    print(f"{a} / {b} == {c}.")