# source/whoops_006.py

def read_float(input_name):
    is_valid = False
    msg_header = ""
    while not is_valid:
        try:
            x = float(input(f"{msg_header}Enter {input_name}: "))
            is_valid = True
        except ValueError:
            msg_header = "Malformed input. "
    return x

if __name__ == "__main__":
    a = read_float("a")
    b = read_float("b")
    while b == 0:
        b = read_float("b")
    c = a / b
    print(f"{a} / {b} == {c}.")