# Read the total number of pies and the number of people
n = int(input())
people = int(input())

# Memoization dictionary to store previously computed results
memo = {}

# Recursive function to solve the problem
def solve(state: list, total: int):
    # Check to see if we can reuse previous calculations
    check = (len(state), state[-1], total)
    if check in memo:
        return memo[check]

    # Base case: last person gets remaining pies, only 1 possibility
    if len(state) == people:
        return 1

    # Determine the minimum number of pies the next person can receive
    min_possible = state[-1]
    res = 0

    if min_possible == 0:  # First person getting pie
        min_possible = 1
        max_possible = n // people
    else:
        max_possible = (n - total) // (people - len(state) + 1)

    # Recursively try all valid states starting from min_possible
    for i in range(min_possible, max_possible + 1):
        new_state = state.copy()
        new_state.append(i)
        res += solve(new_state, total + i)

    # Store the result in the memoization dictionary
    store_state = (len(state), state[-1], total)
    memo[store_state] = res

    return res

# Start the recursion with an initial state and a total of 0
print(solve([0], 0))
