# main.py

from utils import draw_grid, KeyboardListener
from snake import is_game_over, move_snake, update_food, GRID_SIZE
from random import choices
from time import sleep # Sleep is a valuable resource, for both life and CPU threads.

if __name__ == '__main__':
    cx = GRID_SIZE // 2
    snake_len = min(5, GRID_SIZE // 2)
    snake = [(cx, y) for y in range(snake_len - snake_len // 2, 2*snake_len - snake_len // 2)]
    food = list(zip(choices(range(GRID_SIZE), k=20), choices(range(GRID_SIZE), k=20)))
    current_move = 'a' # Initial snake moving direction
    kb_listener = KeyboardListener()
    pressed_key = None
    while not is_game_over(snake):
        draw_grid(GRID_SIZE, snake, food)
        move_snake(snake, food, current_move)
        pressed_key = kb_listener.get_key()
        if pressed_key in ['w', 'a', 's', 'd']:
            current_move = pressed_key
        update_food(food)
        sleep(0.5) # Dummy way to handle FPS rendering

