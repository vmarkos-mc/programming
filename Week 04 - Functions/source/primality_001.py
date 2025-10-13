# source/primality_001.py

n = int(input("Please, enter a positive integer: "))
i = 2
if n < 2:
    print("Not Prime!")
else:
    while n % i != 0:
        i = i + 1
    if n == i:
        print("Prime!")
    else:
        print("Not Prime!")