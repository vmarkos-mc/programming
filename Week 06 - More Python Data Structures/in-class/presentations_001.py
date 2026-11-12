# icex_002

n = int(input('Please enter a positive integer: '))
if n < 0:
    print('You entered a negative integer. Please enter a positive integer.')
    n = int(input('Please enter a positive integer: '))

def proper_divisor_sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
print(proper_divisor_sum(n))


# icex_006

def sqrt_guess(x0, a, e):
    prev_x = x0
    current_x = 0.5 * (prev_x + a / prev_x)
    while abs(current_x - prev_x) >= e:   #(absolute value)
        prev_x = current_x
        current_x = 0.5 * (prev_x + a / prev_x)
    return current_x
print(sqrt_guess(1, 25, 0.0001))
