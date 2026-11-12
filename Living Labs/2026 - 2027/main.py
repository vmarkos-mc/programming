# main.py
# Main entry point for our living game lab

def get_grid_size():
    '''Asks user to provide grid size (s/m/l) and returns the 
    corresponding number of rows/columns as an integer.'''
    # We use the `.lower()` to make sure input is parsed as lower-case characters.
    size = input('Please, enter game grid size (s/m/l): ').lower()
    while size not in ['s', 'm', 'l']:
        size = input('Please, enter game grid size (s/m/l): ').lower()
    if size == 's':
        return 15
    if size == 'm':
        return 20
    return 30

def print_grid(n, player):
    '''Prints game grid'''
    for i in range(n):
        for j in range(n):
            # Recall: rows grow on y, columns grow on x.
            if player == (j, i):
                print('p', end=' ')
            else:
                print('*', end=' ')
        print()

if __name__ == '__main__':
    grid_size = get_grid_size()
    player = (0, grid_size - 1)
    print_grid(grid_size, player)

# A note on coordinate systems.
# In maths we tend to think of the horizontal axis as growing (positive) to the right
# and the vertical axis growing (positive) to the top of the paper / screen.
# In most cases, however, in app design, we revert the y axis to grow towards
# the bottom of the screen. Also, the origin is typically on the top left corner.