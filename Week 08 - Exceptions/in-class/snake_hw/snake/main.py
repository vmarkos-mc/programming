# main.py

using_msvcrt = False

try:
    import curses
except ModuleNotFoundError:
    import msvcrt
    using_msvcrt = True
from snake import is_game_over, init_game, update_game
from time import sleep # Sleep is a valuable resource, for both life and CPU threads.

# FPS = 2 is too low but, well, we are programming a terminal snake
FPS = 2


# In what follows `scr` is a screen object, used by the `curses` library, which 
# is a built-in Python library for handling and building terminal application.
# Do not modify the main function. If you follow things carefully, the following
# should work out of the box.
def main(scr=None):
    if scr is None:
        chrreader = lambda : msvcrt.getch
    else:
        scr.timeout(0)
        chrreader = lambda : scr.getch
    snake, food, current_move = init_game()
    while not is_game_over(snake):
        key = chrreader()
        if key in [97, 100, 115, 119]:
            current_move = chr(key)
        update_game(snake, food, current_move, scr)
        if scr is not None:
            scr.refresh()
        sleep(1 / FPS) # Dummy way to handle FPS rendering


if __name__ == '__main__':
    if using_msvcrt:
        main(None)
    else:
        curses.wrapper(main)
