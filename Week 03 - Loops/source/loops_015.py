# source/loops_015.py

n = int(input("Please, enter an integer: "))
i = 1
p = 1
while i < n:
    p = p * (1 / i ** 0.5)
    i = i + 3
print(p)