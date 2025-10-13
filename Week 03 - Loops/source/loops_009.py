# source/loops_009.py

n = int(input("Please, enter an integer: "))
for i in range(n, 0, -1):
    if i == 1:
        print(i ** 2)
    else:
        print(i ** 2, end = ", ")