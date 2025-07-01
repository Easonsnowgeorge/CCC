# Read the number of elements in the array
n = int(input())
# Read the elements of the array and store them in a list
arr = [int(input()) for _ in range(n)]
# Sort the array to process elements in ascending order
arr.sort()

# Initialize the variable to store the smallest difference
smallest = float('inf')

# Iterate through the array to find the smallest average difference between non-adjacent elements
for i in range(1, n-1):
    # Calculate the average difference between the current element and its non-adjacent neighbors
    smallest = min(smallest, (arr[i+1] - arr[i-1]) / 2)

# Print the smallest difference rounded to 2 decimal places
print(round(smallest, 2))
