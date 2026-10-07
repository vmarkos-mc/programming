# in-class/loops_017a.py

n = int(input("Please, enter an integer: "))
for i in range(2, n + 2, 2):
    if n % i == 0: # This is the logical negation of `n % i != 0`
        break
print(i)