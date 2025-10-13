# source/dictionaries_001.py

if __name__ == "__main__":
    people = dict() # An empty dictionary
    name = input("Enter a name: ")
    while name != "":
        age = int(input(f"Enter {name}'s age: "))
        people[name] = age # Map 'name' to 'age'
        name = input("Enter a name: ")
    needle = input("Enter a name to look for: ")
    found = False
    if needle in people.keys():
        print(f"{needle}'s age is: {people[needle]}")
    else:
        print(f"{needle} not found!")