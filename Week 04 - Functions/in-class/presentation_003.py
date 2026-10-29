k = int(input("please enter first number"))
n = int(input("please enter second number"))
while k > n:
    print("first number must be smaller than second number")
    k = int(input("please enter first number"))
    n = int(input("please enter second number"))
import math
b_c = math.factorial(n) / ((math.factorial(k) * math.factorial(n - k)))
print("result", b_c) 