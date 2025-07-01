# Read the minimum and maximum distances that can be traveled in a day and the number of additional motels
a = int(input())
b = int(input())
n = int(input())

# List of predefined motels and their locations
motel = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

# Add locations of extra motels from input and sort the list
motel.extend([int(input()) for _ in range(n)])
motel.sort()

# Dynamic programming array to store the number of ways to reach each motel
dp = [0] * (len(motel))
dp[0] = 1  # Base case: there is always 1 way to get to the start

# Iterate over each motel to find the number of ways to get to it from earlier motels
for i in range(len(motel)):
    for j in range(i):
        dist = motel[i] - motel[j]
        if a <= dist <= b:  # Check if it's possible to travel from motel j to motel i
            dp[i] += dp[j]

# Print the number of ways to reach the final motel
print(dp[-1])
