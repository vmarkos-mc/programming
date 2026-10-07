# in-class/bitwise-parity.py

# To convert 23 from decimal to binary, we can work in two ways:
#
# First way:
# 1     x --> 1 - 1 = 0     1
# 2     x --> 3 - 2 = 1     1
# 4     x --> 7 - 4 = 3     1
# 8                         0
# 16    x --> 23 - 16 = 7   1
# 32
#
# So, 23 in binary reads: 10111
#
# Second way:
# Repeated division by 2:
# 23 = 2 * 11 + 1
# 11 = 2 * 5  + 1
# 5  = 2 * 2  + 1
# 2  = 2 * 1  + 0
# 1  = 2 * 0  + 1
#
# So, reading moduli bottom-to-top, we get: 10111.
#
# Also, a nice trick in binary: to tell if a number is even or odd by its binary representation
# we can inspect the last digit (units), since even numbers end in 0 while odd in 1.

n = int(input("Please, enter an integer: "))
if n & 1 == 0: # Bitwise AND --> Masking
    print("Even")
else:
    print("Odd")

# An example of masking:
# n = 23, so 10111 in binary
# n & 1, so (using 8-bit representation for each number):
#
#   00010111
# & 00000001
# ----------
#   00000001 --> 1, so 10111 is odd.
#
# Similarly, for n = 24, so 11000 in binary:
#
#   00011000
# & 00000001
# ----------
#   00000000 --> 0, so 11000 is even.