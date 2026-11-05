# main.py

from utils import draw_grid, start_keyboard_listener
from snake import is_game_over, move_snake
from random import sample

if __name__ == '__main__':
    N = 100
    snake = [(x, 0) for x in range(5)]
    foods = list(zip(random.sample(range(100), 20), random.sample(range(100), 20)))
    start_keyboard_listener()
    while not is_game_over():
        pass
