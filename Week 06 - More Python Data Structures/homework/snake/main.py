# main.py

import curses
from utils import draw_grid
from snake import is_game_over, move_snake, update_food, GRID_SIZE
from random import choices
from time import sleep # Sleep is a valuable resource, for both life and CPU threads.


def main(scr):
    scr.timeout(0)
    cx = GRID_SIZE // 2
    snake_len = min(5, GRID_SIZE // 2)
    snake = [(cx, y) for y in range(snake_len - snake_len // 2, 2*snake_len - snake_len // 2)]
    food = list(zip(choices(range(GRID_SIZE), k=20), choices(range(GRID_SIZE), k=20)))
    current_move = 'a' # Initial snake moving direction
    while not is_game_over(snake):
        key = scr.getch()
        if key in [97, 100, 115, 119]:
            current_move = chr(key)
        draw_grid(GRID_SIZE, snake, food, scr)
        move_snake(snake, food, current_move)
        update_food(food)
        scr.refresh()
        sleep(0.5) # Dummy way to handle FPS rendering


if __name__ == '__main__':
    curses.wrapper(main)
