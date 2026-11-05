# snake.py

def cuts_self(snake):
    '''Boolean function returning `True` when a snake cuts itself'''
    return snake[0] in snake[1:]


def move_snake(snake, food, move):
    '''Accepts a snake as a list of points (i.e., 2-tuples), a list of food locations, as a list
    of points and a string wasd movement and modifies in place the snake and updates the food list
    accordingly.
    '''
    new_head = next_point(snake[0], move)
    snake.insert(0, new_head)
    if new_head in food:
        food.remove(new_head)
    else:
        snake.pop()



def next_point(point, move):
    '''Accepts a point (2-tuple) and a wasd movement string and returns the new location
    of that point based on that movement. Bare in mind that x increases left to right while
    y increases top to bottom. So, moving (1,4) right yields (2,4), while moving (1,4) down 
    yields (1,5).'''
    x, y = point # We unpack those values for convenience.
    if move == 'w':
        return (x, y - 1)
    if move == 's':
        return (x, y + 1)
    if move == 'a':
        return (x - 1, y)
    if move == 'd':
        return (x + 1, y)
    return None # Just for clarity: we do not handle any other input and, by default, python functions
    # do return None.


def is_game_over(snake):
    '''Boolean function determining whether a game of Snake is over (True) or not (False)'''
    return cuts_self(snake)
