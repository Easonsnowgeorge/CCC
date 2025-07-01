# Initialize the starting point and a set of used coordinates
point = [-1, -5]
used = {(3, -5), (5, -5), (0, -7), (2, -7), (1, -3), (7, -5), (6, -7), (-1, -5), (4, -7), (3, -3), (5, -3), (0, -2),
        (0, -1), (1, -7), (7, -3), (7, -6), (-1, -6), (4, -5), (3, -7), (3, -4), (5, -7), (5, -4), (0, -3), (2, -3),
        (7, -7), (6, -3), (7, -4), (-1, -7)}

# Read the first move
move = input().split()
danger = False  # Flag to indicate if a danger situation occurs

# Main loop to process moves
while True:
    move[1] = int(move[1])  # Convert the move distance to integer
    x, y = point  # Current coordinates

    # Process left move
    if move[0] == "l":
        for i in range(1, move[1] + 1):
            if (x - i, y) not in used:
                used.add((x - i, y))
            else:
                danger = True
        x -= move[1]

    # Process right move
    elif move[0] == "r":
        for i in range(1, move[1] + 1):
            if (x + i, y) not in used:
                used.add((x + i, y))
            else:
                danger = True
        x += move[1]

    # Process up move
    elif move[0] == "u":
        for i in range(1, move[1] + 1):
            if (x, y + i) not in used:
                used.add((x, y + i))
            else:
                danger = True
        y += move[1]

    # Process down move
    elif move[0] == "d":
        for i in range(1, move[1] + 1):
            if (x, y - i) not in used:
                used.add((x, y - i))
            else:
                danger = True
        y -= move[1]

    # Process quit move
    elif move[0] == "q":
        break

    # Output the result of the move
    if danger:
        print(f"{x} {y} DANGER")
        break
    else:
        print(f"{x} {y} safe")

    # Update the current point and read the next move
    point = [x, y]
    move = input().split()
