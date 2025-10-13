# source/operations_003.py
from timeit import timeit # To time stuff

if __name__ == "__main__":
    N = 100000
    a = []
    b = []
    c = []
    lst_append = timeit(lambda : a.append(4), number = N)
    insert_end = timeit(lambda : b.insert(-1, 4), number = N)
    insert_start = timeit(lambda : c.insert(0, 4), number = N)
    print(f"append:       {lst_append}\ninsert end:   {insert_end}\ninsert start: {insert_start}")