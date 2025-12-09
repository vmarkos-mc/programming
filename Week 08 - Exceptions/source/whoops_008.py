# source/whoops_008.py

if __name__ == "__main__":
    while True:
        try:
            s = input("Guess what I am thinking: ")
            print("Wrong! Try again or quit (Ctrl + C).")
        except KeyboardInterrupt:
            print("\nNot that easy, right?")
            pass