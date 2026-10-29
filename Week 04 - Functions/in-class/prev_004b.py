# in-class/prev_004b.py

n = int(input('Please, enter an integer: '))

if n > 1:
    for i in range(2, n + 1): # Since 1 and n always divide n
        if n % i == 0 and i != n:
            print(f'{n} is not a prime!')
            break
    if i == n:
        print(f'{n} is prime!')
else:
    print(f'{n} is not a prime!')


# `while` alternative
# if n > 1:
#     i = 2
#     while n % i != 0:
#         i = i + 1
#     if i == n:
#         print(f'{n} is prime!')
#     else:
#         print(f'{n} is not prime!')
# else:
#     print(f'{n} is not a prime!')