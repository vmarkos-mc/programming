# main.py
# Main entry point for our living game lab

from random import randrange

def get_grid_size():
    '''Asks user to provide grid size (s/m/l) and returns the 
    corresponding number of rows/columns as an integer.'''
    # We use the `.lower()` to make sure input is parsed as lower-case characters.
    size = input('Please, enter game grid size (s/m/l): ').lower()
    while size not in {'s', 'm', 'l'}:
        size = input('Please, enter game grid size (s/m/l): ').lower()
    if size == 's':
        return 15
    if size == 'm':
        return 20
    return 30


def generate_relics(n):
    '''Generates a set of randomly chosen points, serving as relic locations.'''
    relics = set()
    while len(relics) < n:
        x = randrange(n)
        y = randrange(n)
        # Since this is a set, this is not guaranteed to add a new element all the time.
        relics.add((x, y))
    return relics


def get_next_move():
    '''Gets next move from user and returns it as "wasd".'''
    move = input().lower() # Just ask for the move, no message printed
    while move not in {'w', 'a', 's', 'd', 'q'}: # 'q' for quitting
        move = input().lower()
    return move


def make_move(player, move, grid_size):
    '''Given a player (point as tuple), a move string ('wasd') and the 
    current grid size (int), it returns the new player position, clamping
    the player into the grid.'''
    x, y = player # Tuple unpacking
    if move == 'w' and y > 0:
        return (x, y - 1)
    if move == 's' and y < grid_size - 1:
        return (x, y + 1)
    if move == 'a' and x > 0:
        return (x - 1, y)
    if move == 'd' and x < grid_size - 1:
        return (x + 1, y)
    # In case the requested move is not possible
    return player


def print_grid(n, player, visited, printover=True):
    '''Prints game grid'''
    if printover:
        print('\x1b[H\x1b[2B')
    for i in range(n):
        for j in range(n):
            # Recall: rows grow on y, columns grow on x.
            if player == (j, i):
                print('p', end=' ')
            elif (j, i) in visited:
                print('.', end=' ')
            else:
                print('*', end=' ')
        print()


if __name__ == '__main__':
    grid_size = get_grid_size()
    player = (0, grid_size - 1)
    visited = { player }
    relics = generate_relics(grid_size)
    print_grid(grid_size, player, visited, printover=False)
    move = get_next_move()
    while move != 'q':
        player = make_move(player, move, grid_size)
        visited.add(player)
        print_grid(grid_size, player, visited)
        move = get_next_move()
    print('Game over!')

# A note on coordinate systems.
# In maths we tend to think of the horizontal axis as growing (positive) to the right
# and the vertical axis growing (positive) to the top of the paper / screen.
# In most cases, however, in app design, we revert the y axis to grow towards
# the bottom of the screen. Also, the origin is typically on the top left corner.