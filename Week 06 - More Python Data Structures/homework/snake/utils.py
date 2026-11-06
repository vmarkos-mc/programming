# utils.py

# Used for listening to key presses
from pynput import keyboard

# Not the best idea to use globals that way, but we will discuss better ways at the 
# end of the semester
SNAKE_PT = 'o'
FOOD_PT = '+'
EMPTY_PT = ' '


def draw_grid(n, snake, food):
    '''Draws a grid including the snake and related food instances'''
    print('\x1b[1;37;40m', end='')
    for i in range(n):
        for j in range(n):
            if (i, j) in snake:
                print(SNAKE_PT, end=' ')
            elif (i, j) in food:
                print(FOOD_PT, end=' ')
            else:
                print(EMPTY_PT, end=' ')
        print() # As usual, just to change lines.
    print(f'\x1b[{n}A\x1b[{n}D', end='')


class KeyboardListener:
    '''Utility class implementing a keyboard listener'''
    def __init__(self):
        self.last_key = None
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()


    def _on_press(self, key):
        try:
            self.last_key = key.char.lower()
        except AttributeError:
            pass


    def get_key(self):
        key = self.last_key
        self.last_key = None
        return key

