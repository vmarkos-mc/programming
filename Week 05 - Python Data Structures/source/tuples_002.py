# source/tuples_002.py
if __name__ == "__main__":
    people = []
    name = input("Enter a name: ")
    while name != "":
        age = int(input(f"Enter {name}'s age: "))
        people.append((name, age)) # Append a tuple to our list
        name = input("Enter a name: ")
    needle = input("Enter a name to look for: ")
    found = False
    for name, age in people:
        if needle == name:
            print(f"{needle}'s age is: {age}")
            found = True
            break
    if not found:
        print(f"{needle} not found!")