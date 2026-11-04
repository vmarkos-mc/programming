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
    for i in range(n):
        for j in range(n):
            if (i, j) in snake:
                print(SNAKE_PT, end=' ')
            elif (i, j) in food:
                print(FOOD_PT, end=' ')
            else:
                print(EMPTY_PT, end=' ')
        print() # As usual, just to change lines.


def start_keyboard_listener():
    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            return ''
        if key_char in 'wasd':
            return key_char
        return ''
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
