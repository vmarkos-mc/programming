# in-class/imperial_to_metric.py

# Ask for user input, casting it into float
dist_in_feet = float(input('Enter distance in feet: '))
# Convert feet to metres using the given formula
dist_in_metres = dist_in_feet * 0.3084
# Print the results in a pretty manner
print(dist_in_feet, 'feet =', dist_in_metres, 'metres.')