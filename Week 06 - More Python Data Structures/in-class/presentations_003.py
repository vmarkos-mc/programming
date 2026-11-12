moves = 0

def tower_of_hanoi(n, source, auxiliary, destination):
    global moves

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        moves += 1
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)
    moves += 1

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter the number of disks: "))

if n > 0:
    tower_of_hanoi(n, 'A', 'B', 'C')
    print("Total number of moves:", moves)
else:
    print("Please enter a positive integer.")
