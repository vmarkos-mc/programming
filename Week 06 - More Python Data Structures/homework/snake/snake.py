# snake.py

from random import random, choice, choices
from utils import draw_grid

# You can change the following for testing or just to make the game more interesting.
GRID_SIZE = 10 # Side size of the square grid.
P_ADD_FOOD = 0.1 # Probability to add a new food on the grid.
N_FOOD = 20 # Number of food instances to be added on the grid initially.

def cuts_self(snake):
    '''Boolean function returning `True` when a snake cuts itself'''
    # Implement this!
    pass


def move_snake(snake, food, move):
    '''Accepts a snake as a list of points (i.e., 2-tuples), a list of food locations, as a list
    of points and a string wasd movement and modifies in place the snake and updates the food list
    accordingly.
    '''
    # Implement this!
    pass


def next_point(point, move):
    '''Accepts a point (2-tuple) and a wasd movement string and returns the new location
    of that point based on that movement. Bare in mind that x increases left to right while
    y increases top to bottom. So, moving (1,4) right yields (2,4), while moving (1,4) down 
    yields (1,5).'''
    # Well, implement this!
    pass


def update_food(food):
    '''Accepts a list of points corresponding to food locations and updates it by
    possibly adding some food with some probability P_ADD_FOOD.
    
    Mathematical addendum: This approach does not pick new food points uniformly at
    random. To do so, we could implement reservoir sampling, or similar alternatives.
    Here, instead, we strive for simplicity.'''
    # README: Do not modify this function!
    if random() > P_ADD_FOOD: # At random, determine whether to add new food or not
        return
    food_point = (choice(range(GRID_SIZE)), choice(range(GRID_SIZE)))
    while food_point in food:
        food_point = (choice(range(GRID_SIZE)), choice(range(GRID_SIZE)))
    food.append(food_point)


def is_game_over(snake):
    '''Boolean function determining whether a game of Snake is over (True) or not (False)'''
    # This will be the easiest one, probably. Yet, implement this!
    pass


def init_game():
    '''Game initialisation function'''
    # Fill in the rest of the logic and make sure to populate all three 
    # variables in the return statement, below.
    return snake, food, current_move
   

def update_game(snake, food, current_move, scr):
    '''Game update function, updating all related game entities. `scr` is just the game screen'''
    # README: Do not change this function! Instead, you can use it as a guide.
    draw_grid(GRID_SIZE, snake, food, scr)
    move_snake(snake, food, current_move)
    update_food(food)

