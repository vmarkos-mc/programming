# source/whoops_004.py
if __name__ == "__main__":
    is_valid = False
    while not is_valid:
        try:
            a = float(input("Enter a: "))
            is_valid = True
        except ValueError:
            pass
    b = float(input("Enter b: "))
    while b == 0:
        b = float(input("Invalid value, b == 0! Enter b: "))
    c = a / b
    print(f"{a} / {b} == {c}.")