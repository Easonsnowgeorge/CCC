from itertools import combinations

# Read the number of people in the graph
n = int(input())
graph = [[] for _ in range(n+1)]  # Directed Acyclic Graph (DAG)

# Construct the graph based on input
for i in range(1, n):
    p = int(input())
    graph[p].append(i)

# Depth-First Search (DFS) function to find all people invited by a person
def dfs(n):
    stack = [n]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        stack.extend(graph[node])
    return visited

# Generate a list of people invited by each person
pieces = []
for i in range(1, n):
    pieces.append(dfs(i))

# Generate all combinations of groups
all_combs = []
for i in range(1, n):
    all_combs.extend(combinations(pieces, i))

# Count the number of valid combinations
res = 1  # Initialize with 1 to account for the empty combination
for comb in all_combs:
    valid = True
    seen = set()
    for group in comb:
        for i in group:
            if i in seen:
                valid = False
                break
            else:
                seen.add(i)
    if valid:
        res += 1

# Print the total number of valid combinations
print(res)
