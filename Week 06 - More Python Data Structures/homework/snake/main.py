# main.py

from utils import draw_grid, start_keyboard_listener
from snake import is_game_over, move_snake, update_food, GRID_SIZE
from random import sample
from time import sleep # Sleep is a valuable resource, for both life and CPU threads.

if __name__ == '__main__':
    snake = [(x, 0) for x in range(5)]
    food = list(zip(sample(range(GRID_SIZE), 20), sample(range(GRID_SIZE), 20)))
    current_move = 'a' # Initial snake moving direction
    kb_listener = start_keyboard_listener()
    while not is_game_over():
        draw_grid(GRID_SIZE, snake, food)
        move_snake(current_move)
        if kb_listener: # Double check this returns the on_press listener
            current_move = kb_listener
        update_food(food)
        sleep(0.5) # Dummy way to handle FPS rendering

