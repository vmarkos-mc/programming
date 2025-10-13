# source/loops_010.py

n = int(input("Please, enter an integer: "))
for i in range(n, 0, -1):
    print(i ** 2, end = ", " if i > 1 else "\n")