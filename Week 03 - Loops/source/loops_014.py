# source/loops_014.py

n = int(input("Please, enter an integer: "))
m = int(input("Please, enter an integer: "))
for i in range(n):
    for j in range(m):
        print(i, j, sep = "-", end = " ")
    print()