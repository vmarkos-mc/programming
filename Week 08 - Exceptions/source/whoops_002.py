# source/whoops_002.py

if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    while b == 0:
        b = float(input("Invalid value, b == 0! Enter b: "))
    c = a / b
    print(f"{a} / {b} == {c}.")