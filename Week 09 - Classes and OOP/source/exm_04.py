class Pet:
    def __init__(self, name = "John Doe"):
        self.name = name
        self.location = 0
        self.is_playing = False

    def talk(self):
        """
        This provides some default implementation of pet "talking"
        which is intended to be overwritten by any ancestors.
        """
        print(f"{self.name} talks.")

    def walk(self):
        """Both our pets walk!"""
        self.location += 1
        print(f"{self.name} walks!")

    def play(self):
        self.is_playing = True
        print(f"{self.name} is playing!")

    def stop_playing(self):
        self.is_playing = False
        print(f"{self.name} has stopped playing!")

    def play_with(self, other):
        self.play()
        other.play()
        print(f"{self.name} is playing with {other.name}!")

class Dog(Pet):
    def __init__(self, name = "John Doe"):
        super().__init__(name) # It is mandatory in child classes to call the parent initialiser through `super()`
        self.is_there_mess = False # We add a new object field.

    def produce_mess(self): # This is a dog specific function. Pets in general don't do this!
        self.is_there_mess = True
        print(f"{self.name} has made some mess!")

    def run(self):
        self.location += 3

    def talk(self):
        """
        This is over-writing. We are re-defining an object function in a child 
        class so that it does something different from its parent instance.
        """
        print(f"{self.name} barks!")

class Cat(Pet):
    def __init__(self, name = "John Doe"):
        super().__init__(name) # It is mandatory in child classes to call the parent initialiser through `super()`
        self.is_in_cleaning_mode = False # We add a new object field.

    def clean(self): # This is a cat specific function. Pets in general don't do this!
        if self.is_playing:
            self.is_playing = False
        self.is_in_cleaning_mode = True
        print(f"{self.name} is cleaning itself!")

    def stop_cleaning(self):
        self.is_in_cleaning_mode = False
        print(f"{self.name} has stopped cleaning itself!")

    def talk(self):
        """
        This is over-writing. We are re-defining an object function in a child 
        class so that it does something different from its parent instance.
        """
        print(f"{self.name} purrs!")

    def play(self):
        """
        We need to over-write this to make sure a cat is not playing and 
        cleaning itself at the same time.
        """
        if self.is_in_cleaning_mode:
            self.is_in_cleaning_mode = False
        super().play() # We can then call parent's `play()` to complete the job.

def main():
    alice = Dog()
    bob = Cat()
    charlie = Pet()
    bob.talk()
    alice.talk()
    bob.clean()
    bob.play()
    alice.play_with(bob)
    charlie.play_with(alice)
    charlie.talk()
    # Uncomment this:
    # charlie.clean()

if __name__ == "__main__":
    main()