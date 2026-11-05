# in-class/icex_001.py

# source/dictionaries_001.py

if __name__ == "__main__":
    people = dict() # An empty dictionary
    name = input("Enter student name: ")
    while name != "":
        age = int(input(f"Enter {name}'s grade: "))
        people[name] = age # Map 'name' to 'age'
        name = input("Enter student name: ")
    needle = input("Enter student name to look for: ")
    found = False
    if needle in people.keys():
        print(f"{needle}'s grade is: {people[needle]}")
    else:
        print(f"{needle} not found!")