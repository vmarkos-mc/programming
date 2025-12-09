from exm_04 import Pet, Dog, Cat # Make sure this file lives at the very same directory as `exm_04.py`!

def main():
    alice = Dog("Alice")
    print(f"Is {alice.name} a dog? {isinstance(alice, Dog)}.")
    print(f"Is {alice.name} a cat? {isinstance(alice, Cat)}.")
    print(f"Is {alice.name} a pet? {isinstance(alice, Pet)}.")
    print(alice.__super__().talk())

if __name__ == "__main__":
    main()