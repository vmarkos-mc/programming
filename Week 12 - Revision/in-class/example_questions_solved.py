# in-class/example_questions_solved.py

import math
import json

with open('list.json', 'r') as file:
    a = json.load(file)

with open('grid.json', 'r') as file:
    grid = [[int(x) for x in row] for row in json.load(file)]

def question_1():
    numbers = range(3, 456)  # 456 to include 455
    # s = sum(numbers) # Using the built-in sum function
    s = 0
    for n in numbers:
        s = s + n
    print(f"Sum: {s}\nMultiplied by 42: {42 * s}")


def question_2():
    string = "Programminginpython"
    s = 0
    for c in string:
        s = s + ord(c)
    print(f"Ordinal sum value of {string}: {s}.")
    # print(sum(map(ord, string))) # Pythonic way using `map()`


def question_3():
    n = 1000
    previous = 0
    current = 1
    # We use `_` to indicate that we do not care for the counter's value
    for _ in range(n - 2):
        next_term = previous + current
        previous = current
        current = next_term
    print(f"The {n}-th Fibonacci term is: {current}")


def question_4():
    def attempt_1(ls):
        max_prod = -math.inf
        for i, x in enumerate(ls):  # i: index, x: ls[i]
            for j, y in enumerate(ls):  # j: index, y: ls[j]
                # Since Python 3.10+ we can use the Walrus operator
                # which assigns a value on a variable while evaluating
                # another expression (like C).
                if i != j and (z := x * y) > max_prod:
                    max_prod = z
        return max_prod

    # Second atempt
    def attempt_2(ls):
        mins = [math.inf, math.inf]
        maxs = [-math.inf, -math.inf]
        for x in ls:
            # Update the two min elements
            if x < mins[0]:
                mins[1] = mins[0]
                mins[0] = x
            elif x < mins[1]:
                mins[1] = x
            # Update the two max elements
            if x > maxs[0]:
                maxs[1] = maxs[0]
                maxs[0] = x
            elif x > maxs[1]:
                maxs[1] = x
        mins_prod = mins[0] * mins[1]
        maxs_prod = maxs[0] * maxs[1]
        if mins_prod > maxs_prod:
            return mins_prod
        return maxs_prod

    s_1 = attempt_1(a)
    s_2 = attempt_2(a)
    print(f"Attempt_1: {s_1}.\n" f"Attempt_2: {s_2}.")


def question_5():
    max_prod = -math.inf
    for i, x in enumerate(a[:-2]):
        y = a[i + 2]
        if x * y > max_prod:
            max_prod = x * y
        # max_prod = x * y if x * y > max_prod else max_prod
    print(f"Max product: {max_prod}.")
    # Using zip
    m = max(map(lambda x: x[0] * x[1], zip(a[:-2], a[2:])))
    print(f"Functional approach: {m}")

def question_6():
    max_prod = -math.inf
    def prod(ls):
        p = 1
        for x in ls:
            p = p * x
        return p
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if j <= len(row) - 4 and (p := prod(row[j:j + 4])) > max_prod:
                max_prod = p
            # if i <= len(grid) - 4 and (p := x * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]) > max_prod:
            if i <= len(grid) - 4 and (p := prod([grid[k][j] for k in range(i, i + 4)])) > max_prod:
                max_prod = p
    print(f"Max product: {max_prod}.")


if __name__ == "__main__":
    valid_input = False
    while not valid_input:
        try:
            qn = int(input(f"Enter question number (1-6): "))
            valid_input = True
        except ValueError:
            pass
    question_map = {
        1: question_1,
        2: question_2,
        3: question_3,
        4: question_4,
        5: question_5,
        6: question_6,
    }
    question_fn = question_map[qn]
    question_fn()
