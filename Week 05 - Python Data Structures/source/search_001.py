# source/search_001.py

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter a number to look for: "))
    if d == a or d == b or d == c:
        print(True)
    else:
        print(False)