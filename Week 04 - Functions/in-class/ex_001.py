# in-class/ex_001.py

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# More compact way
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

# Even more compact way
# def is_even(n):
#     return n % 2 == 0


if __name__ == '__main__':
    m = int(input('Please, enter an integer: '))
    print(f'Is {m} even? {is_even(m)}')