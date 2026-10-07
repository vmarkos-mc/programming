# last-time/in_class_001.py

n = int(input("Please, enter a non-negative integer: "))

# Sanity check
while n < 0:
    n = int(input("Please, enter a *non-negative* integer: "))

# Initialise sum variable at 0.
s = 0

# range(n) would yield 0, 1, 2, ..., n-1
for i in range(n + 1):
    s = s + 1 / 2 ** i # Add one term at a time

print(f"s = {s}.")

# Approach 1: (for the second alternating sum)

s_odd = 0
s_even = 0

# Loop for the even powers of 2
for i in range(0, n + 1, 2):
    s_even = s_even + 1 / 2 ** i

# Loop for the odd powers of 2
for i in range(1, n + 1, 2):
    s_odd = s_odd + 1 / 2 ** i

# Subtract to obtain the final sum
s = s_even - s_odd
print(f"Approach 1: s = {s}.")

# Approach 2: Using a single for loop

s = 0

for i in range(n + 1):
    if i % 2 != 0:
        s = s - 1 / 2 ** i
    else:
        s = s + 1 / 2 ** i

print(f"Approach 2: s = {s}.")

# Approach 3: Avoiding if

s = 0

# The trick here is that the powers of (-1) alternate between
# -1 (odd powers) and 1 (even powers).
for i in range(n + 1):
    s = s + (-1) ** i * 1 / 2 ** i

print(f"Approach 3: s = {s}.")