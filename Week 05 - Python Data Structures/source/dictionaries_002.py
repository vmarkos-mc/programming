# source/dictionaries_002.py
from timeit import timeit
from random import randint

def list_search(l, key):
    for l_key, value in l:
        if l_key == key:
            return value
    return -1

if __name__ == "__main__":
    L = 0; U = 10000; N = U - L + 1
    a = { x: randint(L, U) for x in range(N) }
    b = [ (x, randint(L, U)) for x in range(N) ]
    dict_time = timeit(lambda : a[randint(L, U)], number = U - L)
    list_time = timeit(lambda : list_search(b, randint(L, U)), number = U - L)
    print(f"dict: {dict_time}\nlist: {list_time}")