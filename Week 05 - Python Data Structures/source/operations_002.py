# source/operations_002.py
from timeit import timeit # To time stuff

if __name__ == "__main__":
    N = 100000
    a = [x for x in range(N)] # a = [0,1,...,N-1]
    b = [x for x in range(N)] # b = [0,1,...,N-1]
    c = [x for x in range(N)] # c = [0,1,...,N-1]
    pop_last = timeit(lambda : a.pop(), number = N)
    pop_first = timeit(lambda : b.pop(0), number = N)
    pop_middle = timeit(lambda : c.pop(len(c) // 2), number = N)
    print(f"last:   {pop_last}\nfirst:  {pop_first}\nmiddle: {pop_middle}")