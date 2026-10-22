# in-class/icex_001.py

n = int(input('Please, enter n: '))

s = 0 # sum
for i in range(n + 1): # We want i = 0,1,2,...,n
    s = s + 1 / 2 ** i
print(s)

s = 0
for i in range(n + 1):
    if i % 2 == 0: # Add the even powers of two
        s = s + 1 / 2 ** i
    else: # Subtract the odd powers of two
        s = s - 1 / 2 ** i
print(s)

s = 0
for i in range(n + 1):
    # (-1) ** i:
    # i         0   1   2   3   4   5
    # (-1)**i   1  -1   1  -1   1  -1   
    s = s + (-1) ** i * 1 / 2 ** i
print(s)

# Using a while loop:
# i = 0
# while i <= n:
#     s = s + 1 / 2 ** i
#     i = i + 1