# in-class/icex_001.py

n = int(input('Please, enter n: '))

s = 0 # sum
for i in range(n + 1): # We want i = 0,1,2,...,n
    s = s + 1 / 2 ** i
print(s)

# Using a while loop:
# i = 0
# while i <= n:
#     s = s + 1 / 2 ** i
#     i = i + 1