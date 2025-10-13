# source/search_003.py

def search(needle, haystack):
    for x in haystack:
        if needle == x:
            return True # This breaks the loop too
    return False

if __name__ == "__main__":
    haystack = []
    n = int(input("Enter a positive integer: "))
    while n > 0:
        haystack.append(n)
        n = int(input("Enter a positive integer: "))
    needle = int(input("Enter a number to look for: "))
    print(search(needle, haystack))