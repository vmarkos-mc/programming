# in-class/ex_001.py

tutorials = int(input('Please, enter number of tutorials to attend: '))
# Optional validity check
while tutorials <= 0:
    tutorials = int(input('Please, enter number of tutorials to attend: '))

if tutorials <= 5:
    cost = 0.0
elif tutorials <= 15: # 5 + 10
    cost = (tutorials - 5) * 5.0
elif tutorials <= 35: # 5 + 10 + 20
    cost = 10 * 5.0 + (tutorials - 15) * 4.0
else:
    cost = 10 * 5.0 + 20 * 4 + (tutorials - 35) * 2.5

print(f'Total cost: {cost} $.')