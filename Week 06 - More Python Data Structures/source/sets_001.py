# source/sets_001.py

if __name__ == "__main__":
    a = set([1, 3, 4, 6]) # Initialise a set from a list
    b = { 1, 4, 7, 9 } # Initialise a set directly
    print(a.intersection(b))
    print(a.union(b))
    print(a.difference(b))
    print(a.symmetric_difference(b))