# source/loops_012.py

n = int(input("Please, enter an integer: "))
s = 0
for i in range(1, n + 1, 2):
    s = s + 1 / i ** 2
print(s)