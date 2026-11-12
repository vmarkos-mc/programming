def div_sum(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total

numbers = {}

while True:
    n = int(input("give a positive integer"))

    if n <= 0:
        break

    numbers[n] = div_sum(n)

while True:
    n = int(input("give a number to find its divisor sum "))

    if n <= 0:
        break

    if n in numbers:
        print("Sum of divisors", numbers[n])
    else:
        print("Number was not entered")
