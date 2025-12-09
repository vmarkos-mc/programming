# source/whoops_005.py

if __name__ == "__main__":
    is_valid = False
    msg_header = ""
    while not is_valid:
        try:
            a = float(input(f"{msg_header}Enter a: "))
            is_valid = True
        except ValueError:
            msg_header = "Malformed input. "
    b = float(input("Enter b: "))
    while b == 0:
        b = float(input("Invalid value, b == 0! Enter b: "))
    c = a / b
    print(f"{a} / {b} == {c}.")