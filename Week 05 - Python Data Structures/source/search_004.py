# source/search_004.py

if __name__ == "__main__":
    haystack = []
    n = int(input("Enter a positive integer: "))
    while n > 0:
        haystack.append(n)
        n = int(input("Enter a positive integer: "))
    needle = int(input("Enter a number to look for: "))
    if needle in haystack:
        print(True)
    else:
        print(False)