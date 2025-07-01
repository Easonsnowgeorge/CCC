# List to store the input data
data = []
# Loop to read input until "halt" is encountered
while True:
    x = input()
    if x == "halt":
        break
    else:
        data.append(x)

# Dictionary mapping each letter to its corresponding keypress sequence on a keypad
values = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777", "s": "7777",
    "t": "8", "u": "88", "v": "888",
    "w": "9", "x": "99", "y": "999", "z": "9999"
}

# Loop through each word in the input data
for i in range(len(data)):
    count = 0  # Counter for the total keypresses
    word = data[i]  # Current word to process
    for x in range(len(word)):
        if x == 0:
            count += len(values[word[x]])  # Count the keypresses for the first letter
        elif (values[word[x]])[0] == (values[word[x-1]])[0]:
            count += 2  # Pause for 2 seconds if consecutive letters are on the same key
            count += len(values[word[x]])  # Add the keypresses for the current letter
        else:
            count += len(values[word[x]])  # Add the keypresses for the current letter
    print(count)  # Print the total keypresses for the word
