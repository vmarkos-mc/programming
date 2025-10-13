# source/search_002.py

def search(needle, haystack):
    for i in range(len(haystack)):
        if needle == haystack[i]:
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