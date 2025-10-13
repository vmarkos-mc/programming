# source/loops_011.py

n = int(input("Please, enter an integer: "))
s = 0
for i in range(1, n + 1):
    s = s + 1 / i ** 2
print(s)