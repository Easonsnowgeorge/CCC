# Function to print elements of a 2D list (flowers) in a formatted way
def print_flowers(flowers):
    for i in flowers:
        out = ""
        for j in i:
            out += j + " "
        print(out[:-1])  # Removes the last space and prints the line

# Function to determine the type of transformation needed based on the first two elements
def check(flowers):
    if int(flowers[0][0]) > int(flowers[0][1]):
        if int(flowers[0][0]) > int(flowers[1][0]):
            return 2
        else:
            return 3
    else:
        if int(flowers[0][0]) < int(flowers[1][0]):
            return 0
        else:
            return 1

# Input length of the 2D list (flowers)
length = int(input())
flowers = []

# Reading each flower (row) and adding to the 2D list (flowers)
for i in range(length):
    flower = input().split()
    flowers.append(flower)

# Rotate or flip the 2D list based on the check function's output
for i in range(check(flowers)):
    flowers = list(zip(*flowers[::-1]))

# Print the transformed 2D list
print_flowers(flowers)
