# in-class/last_time.py

def lower_triangle(n):
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


def empty_square(n):
    for i in range(n): # Runs through rows
        for j in range(n): # Runs through columns
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

if __name__ == '__main__':
    n = int(input('Please, enter n: '))
    lower_triangle(n)
    print('=' * 20)
    empty_square(n)
