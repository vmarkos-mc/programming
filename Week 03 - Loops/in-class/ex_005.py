# in-class/ex_005.py

# Ask for user input
n = int(input('Enter n: '))
while n <= 0:
    n = int(input('Enter n: '))

i = 1 # Counter, looking for divisors
while i <= n:
    # If i divides n...
    if n % i == 0:
        # print `i`
        print(i, end=' ')
    i = i + 1 # i += 1

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)