#icex_002

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = b  # a = b - a 
        b = a + b
        a = c
        
    return b
print(fibonacci(9))


#icex_008

n = int(input('Please enter the size of the rows and columns: '))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()


#icex_007

r = int(input('Number of rows: '))
for row in range(1, r + 1):
    for i in range(r - row):
        print(' ', end='')
    for i in range(row):
        print('* ', end='')
    print()
