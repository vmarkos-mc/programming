# source/loops_018.py

n = int(input("Please, enter an integer: "))
for i in range(2, n + 2, 2):
    if n % i == 0:
        break
print(i)