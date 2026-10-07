# last-time/in_class_006.py

n = int(input("Please, enter the number of rows / columns: "))
m = 1

for row in range(n):
    for col in range(n):
        if col < n - m: # More straightforward implementation
        # if col + row < n - 1: # Alternative way
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print() # This is used to change line
    m = m + 1