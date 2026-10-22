# in-class/ex_002.py

n = int(input('Please, enter n: '))
if n > 10:
    print('What?')
else:
    print('Well...')

# Observe that the intermediate conditions in the `elif` statements
# are not reachable, since they are sub-cases of `n > 10`. So, we can just
# omit those...