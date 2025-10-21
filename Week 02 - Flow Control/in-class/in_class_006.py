# in-class/in_class_006.py

n = int(input("Please, enter a positive integer: "))
while n <= 0:
    n = int(input("Please, enter a positive integer: "))

divisors_sum = 0
m = 1 # The first divisor we should check
while m < n: # Stop at n-1, to ignore n.
    # If m divides n...
    if n % m == 0:
        divisors_sum = divisors_sum + m
        # divisors_sum += m # The same as above, just shorter
    m = m + 1 # Proceed to the next candidate divisor

if n == divisors_sum:
    print(f"{n} is perfect!")
else:
    print(f"{n} is not perfect!")