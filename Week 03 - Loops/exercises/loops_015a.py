# in-class/loops_015a.py

n = int(input("Please, enter an integer: "))
p = 1
for i in range(1, n, 3):
    p = p * (1 / i ** 0.5)
print(p)