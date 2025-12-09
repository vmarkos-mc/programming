def bark():
    print(f"Woof!")

def walk(loc):
    new_loc = loc + 1 # Walking means +1 meter (?)
    print(f"I am now at position: {new_loc}")
    return new_loc

def run(loc):
    new_loc = loc + 3 # Dogs run three times faster than they walk (?)
    print(f"I am now at position: {new_loc}")
    return new_loc

def produce_mess():
    print(f"I have made some mess! ")
    return True

def main():
    location = 0 # Assume that the dog moves in one dimension, for simplicity.
    is_there_mess = False # A flag to help us know when we should clean up some dog mess.
    bark()
    bark()
    location = walk(location)
    location = run(location)
    location = walk(run(location))
    is_there_mess = produce_mess()

if __name__ == "__main__":
    main()