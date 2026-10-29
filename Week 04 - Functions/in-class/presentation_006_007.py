# in class exercise #006

n = int(input('Please enter a positive integer: '))

while n <= 0:
    print('That is not a positive integer. Please try again.')
    n = int(input('Please enter a positive integer: '))

total = 0 
for m in range(1, n):
    if n % m == 0:
        total = total + m

if total == n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')



# in class exercise #007

a = int(input('Please enter a positive integer: '))
b = int(input('Please enter a positive integer: '))

total_a = 0
for m in range(1, a):
    if a % m == 0:
        total_a = total_a + m

total_b = 0
for m in range(1, b):
    if b % m == 0:
        total_b = total_b + m

if total_a == b and total_b == a:
    print(f'{a} and {b} are amicable numbers')
else:
    print(f'{a} and {b} are not amicable numbers')
