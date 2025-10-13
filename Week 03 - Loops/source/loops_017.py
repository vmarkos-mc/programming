# source/loops_017.py

n = int(input("Please, enter an integer: "))
i = 2
while i < n and n % i != 0:
    i = i + 2
print(i)