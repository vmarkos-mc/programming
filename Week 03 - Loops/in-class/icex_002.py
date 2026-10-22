# in-class/icex_002.py

n = int(input('Please, enter n: '))

f = 1
for i in range(1, n + 1): # We want to multiply 1*2*...*n
    f = f * i
print(f)