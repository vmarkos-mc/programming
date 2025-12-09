class Dog:
    def __init__(self):
        """
        This is an initialiser. We use `__init__()` to explain to python how a 
        Dog should look like once it is "born". This means that every instance of class
        Dog will have a location at zero and no mess produced.
        """
        self.location = 0
        self.is_there_mess = False

    def bark(self):
        """
        When it comes to object methods (i.e., functions belonging to a certain object), 
        we have to always pass `self` as a first argument. `self` is a pointer to 
        ourselves, i.e., to the very specific **instance** this method (function) is 
        called from.
        """
        print(f"Woof!")

    def walk(self):
        """
        Since `location` is a field of each Dog object, it means that we need not 
        return anything. All information needed is kept within the class!
        """
        self.location = self.location + 1
        print(f"I am now at position: {self.location}")

    def run(self):
        self.location = self.location + 3
        print(f"I am now at position: {self.location}")

    def produce_mess(self):
        self.is_there_mess = True
        print(f"I have made some mess!")

def main():
    alice = Dog() # This creates an instance of class Dog that has the default properties determined by `__init__()`.
    bob = Dog()
    alice.bark()
    bob.bark()
    alice.walk()
    bob.run()
    bob.produce_mess()
    print(f"Alice is at: {alice.location}, while Bob is at: {bob.location}.")

if __name__ == "__main__":
    main()