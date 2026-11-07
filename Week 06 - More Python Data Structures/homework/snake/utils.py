# utils.py


# Not the best idea to use globals that way, but we will discuss better ways at the 
# end of the semester
SNAKE_PT = 'o'
FOOD_PT = '+'
EMPTY_PT = ' '


def draw_grid(n, snake, food, scr):
    '''Draws a grid including the snake and related food instances'''
    print('\x1b[1;37;40m', end='')
    for i in range(n):
        row = ''
        for j in range(n):
            if (i, j) in snake:
                row += f'{SNAKE_PT} '
            elif (i, j) in food:
                row += f'{FOOD_PT} '
            else:
                row += f'{EMPTY_PT} '
        scr.addstr(i, 0, row)
    print(f'\x1b[{n}A\x1b[{n}D', end='')


