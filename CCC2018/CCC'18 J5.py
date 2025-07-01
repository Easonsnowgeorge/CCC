from collections import deque, defaultdict

# This script uses Breadth-First Search (BFS) to find the minimum distance
# to all nodes in a graph and determine if the graph is connected.

# Read the number of nodes in the graph
n = int(input())
graph = defaultdict(list)

# Build the graph as an adjacency list
for i in range(1, n + 1):
    line = input().split()
    graph[str(i)].extend(line[1:])

# BFS function to compute the shortest distance from the start node to all other nodes
def bfs(start):
    q = deque([start])  # Queue for BFS
    visited = set()  # Set to keep track of visited nodes
    distance = {str(i): float('inf') for i in range(1, n + 1)}  # Dictionary to store distances
    distance[start] = 0

    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)

        # Update distances and add adjacent nodes to the queue
        for adjacent in graph[node]:
            distance[adjacent] = min(distance[adjacent], distance[node] + 1)
            q.append(adjacent)

    # Check if all nodes are visited (graph is connected)
    if len(visited) == n:
        print("Y")
    else:
        print("N")
    return distance

# Start BFS from node '1'
d = bfs("1")

# Find the minimum cost to reach a leaf node (a node with no outgoing edges)
min_cost = float('inf')
for node, cost in d.items():
    if not graph[node] and min_cost > cost:
        min_cost = cost

# Add 1 to the cost as the problem might require (based on specific problem conditions)
print(min_cost+1)
