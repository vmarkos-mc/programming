# in-class/prev_005.py

rows = int(input('Please, enter number of rows: '))
while rows <= 0:
    rows = int(input('Please, enter number of rows: '))

cols = int(input('Please, enter number of columns: '))
while cols <= 0:
    cols = int(input('Please, enter number of columns: '))

# Typically, in Python, we name variables using `_` if they are not 
# meant to be used in our program, but just serve as, e.g., counters.
for _ in range(rows): # integers in [0, rows) are `rows` in count
    for _ in range(cols):
        print('*', end=' ')
    print()