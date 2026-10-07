# last-time/in_class_005.py

rows = int(input("Please, enter the number of rows: "))
cols = int(input("Please, enter the number of columns: "))

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print() # This is used to change line