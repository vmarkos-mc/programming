from exm_04 import Pet, Dog, Cat # Make sure this file lives at the very same directory as `exm_04.py`!

def main():
    alice = Dog("Alice")
    bob = Dog("Bob")
    print(f"Are {alice.name} and {bob.name} the same? {alice == bob}")
    another_bob = Dog("Bob")
    print(f"Are {bob.name} and {another_bob.name} the same? {bob == another_bob}")
    charlie = bob # Why create something new when you can copy stuff?
    charlie.name = "Charlie" # Just remember to rename charlie...
    print(f"Charlie is named {charlie.name}.") # Phew...
    print(f"Bob is named {bob.name}.")

if __name__ == "__main__":
    main()