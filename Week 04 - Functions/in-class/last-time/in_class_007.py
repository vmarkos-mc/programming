# last-time/in_class_007.py

n = int(input("Please, enter the number of rows / columns: "))

for row in range(n):
    for col in range(n):
        if row == n - 1 or col == 0:
            print("*", end=" ")
    print() # This is used to change line