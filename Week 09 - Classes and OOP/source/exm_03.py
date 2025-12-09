class Cat:
    def __init__(self, name = "John Doe"):
        self.name = name
        self.location = 0
        self.is_in_cleaning_mode = False
        self.is_in_playing_mode = False

    def clean(self):
        # Clean myself
        if self.is_in_playing_mode:
            self.stop_playing()
        self.is_in_cleaning_mode = True
        print(f"{self.name} is cleaning itself!")

    def stop_cleaning(self):
        # Stop cleaning myself
        self.is_in_cleaning_mode = False
        print(f"{self.name} has stopped cleaning itself!")

    def walk(self):
        self.location += 1 # Cats don't walk that fast with no reason

    def play(self):
        if self.is_in_cleaning_mode:
            self.stop_cleaning()
        self.is_in_playing_mode = True
        print(f"{self.name} is playing!")

    def stop_playing(self):
        self.is_in_playing_mode = False
        print(f"{self.name} has stopped playing!")

    def purr(self):
        print(f"{self.name} says: 'Purr!'.")

    def play_with(self, other):
        self.play()
        other.play()
        print(f"{self.name} is playing with {other.name}!")

def main():
    alice = Cat("Alice")
    bob = Cat("Bob")
    alice.clean()
    alice.play()
    bob.play()
    bob.clean()
    bob.purr()
    alice.walk()
    bob.walk()
    alice.play_with(bob)
    print(f"{alice.name} is at: {alice.location}, while {bob.name} is at: {bob.location}.")

if __name__ == "__main__":
    main()