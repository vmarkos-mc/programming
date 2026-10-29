# in-class/prev_006.py

n = int(input('Please, enter number of rows: '))
while n <= 0:
    n = int(input('Please, enter number of rows: '))

for i in range(n): # integers in [0, rows) are `rows` in count
    # We can just truncate the inner loop:
    # for j in range(n - i):
    # Or, just use an if-clause
    for j in range(n):
        if j < n - i:
            print('*', end=' ')
    print()