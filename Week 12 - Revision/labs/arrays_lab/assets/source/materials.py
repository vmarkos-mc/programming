import random
import string
import math

def foo(n = 100, a = 0, b = 99):
    x = []
    for i in range(n):
        x.append(random.randint(a, b))
    return x

def bar(n = 100, a = 0, b = 99):
    letters = string.ascii_lowercase
    x = dict()
    i = 0
    while i < n:
        key = "".join(random.choice(letters) for _ in range(5))
        if key in x.keys():
            continue
        x[key] = random.randint(a, b)
        i += 1
    return x

def foobar(m = 20, n = 20, a = 0, b = 99):
    x = []
    for i in range(m):
        y = []
        for j in range(n):
            y.append(random.randint(a, b))
        x.append(y)
    return x

def foobaz(x):
    digits = lambda n: math.floor(math.log10(max(n, 1))) + 1
    m = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            d = digits(x[i][j])
            if d > m:
                m = d
    pad = lambda a: " " * (m - digits(a)) + str(a) + " "
    output = ""
    for i in range(len(x)):
        for j in range(len(x[i])):
            output += pad(x[i][j])
        output += "\n"
    return output

if __name__ == "__main__":
    a = foobar()
    b = foobar(15, 15)
    c = foobar(10, 10, 10, 200)
    print(f"a:\n{foobaz(a)}")
    print(f"b:\n{foobaz(b)}")
    print(f"c:\n{foobaz(c)}")