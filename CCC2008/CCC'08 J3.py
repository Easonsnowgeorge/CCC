# Function to find the index of a letter in a GPS-like grid
def index_letter(letter, gps):
    for i in range(len(gps)):
        for j in range(len(gps[i])):
            if gps[i][j] == letter:
                return [i, j]  # Return the row and column indices of the letter

# Define the GPS-like grid
gps = [["A", "B", "C", "D", "E", "F"],
       ["G", "H", "I", "J", "K", "L"],
       ['M', 'N', 'O', 'P', 'Q', 'R'],
       ['S', 'T', 'U', 'V', 'W', 'X'],
       ['Y', 'Z', ' ', '-', '.', 'enter']]

# Read the input and append 'enter' to the list of letters
letters = list(input())
letters.append('enter')

# Initialize the starting position and the total distance
pointer = "A"
total = 0

# Iterate through the letters to calculate the total distance
for i in range(len(letters)):
    first = index_letter(pointer, gps)  # Get the index of the current position
    second = index_letter(letters[i], gps)  # Get the index of the next letter
    # Calculate the distance and add it to the total
    total += abs(first[1] - second[1]) + abs(first[0] - second[0])
    pointer = letters[i]  # Update the current position

# Print the total distance
print(total)
