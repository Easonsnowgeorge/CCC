# Read the first input
x = input().split()
# Loop until the input is ["0"]
while x != ["0"]:
    x = list(map(int, x))  # Convert input strings to integers

    length = x[0]  # Length of the temperature readings
    temps = x[1:]  # Temperature readings
    sequence = []  # List to store differences between consecutive temperatures

    # Extract the sequence of differences
    for i in range(len(temps) - 1):
        sequence.append(temps[i + 1] - temps[i])

    # Flag to check if the shortest sequence is found
    flag = False

    # Try to find the shortest repeating subsequence
    for i in range(1, len(sequence)):
        test = True  # Flag to check if the current subsequence is repeating
        sub = sequence[:i]  # Current subsequence to test
        temp = sequence.copy()  # Copy of the sequence for comparison

        # Check if the subsequence repeats throughout the sequence
        while len(temp) > len(sub):
            if temp[:i] == sub:
                del temp[:i]  # Delete the matching part
            else:
                test = False
                break

        # Check if the remaining part of the sequence matches the subsequence
        if test:
            if temp == sequence[:len(temp)]:
                print(i)  # Print the length of the shortest repeating subsequence
                flag = True
                break

    # If no repeating subsequence is found, print the length of the entire sequence
    if not flag:
        print(len(sequence))

    # Read the next input
    x = input().split()
