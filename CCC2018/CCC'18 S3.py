from collections import deque

# Read the dimensions of the graph and create the graph, distances, and camera visibility matrices
ROWS, COLS = map(int, input().split())
graph = [list(input()) for _ in range(ROWS)]
distances = [[10000 for _ in range(COLS)] for _ in range(ROWS)]
cameras = [[False for _ in range(COLS)] for _ in range(ROWS)]
flag = False  # Flag to indicate if the start cell is covered by a camera

# Directions for camera visibility and BFS traversal
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()

# Handle camera visibility and find the start position
for r in range(ROWS):
    for c in range(COLS):
        cell = graph[r][c]
        if cell == "C":
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                while graph[new_r][new_c] != "W":
                    if graph[new_r][new_c] == ".":
                        cameras[new_r][new_c] = True
                    if graph[new_r][new_c] == "S":
                        flag = True
                    new_r += dr
                    new_c += dc
        if cell == "S":
            q.append((r, c))
            distances[r][c] = 0

# Function to convert conveyors to walls or destination tuples
def conveyor_to_wall(array):
    rows = len(array)
    cols = len(array[0])
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    def dfs(r, c):
        if type(array[r][c]) == tuple:
            return array[r][c]
        elif array[r][c] not in directions:
            return r, c

        direction = array[r][c]
        dr, dc = directions[direction]
        array[r][c] = '#'  # Mark as visited
        res = dfs(r + dr, c + dc)  # Recursive DFS call

        if res == (r, c):
            array[r][c] = 'W'  # Convert to wall in case of cycle
        else:
            array[r][c] = res  # Set to the destination tuple
        return res

    for r in range(rows):
        for c in range(cols):
            if array[r][c] in directions:
                dfs(r, c)
                if array[r][c] == 'W':
                    array[r][c] = 'W'
    return array

# Process the graph to handle conveyors and start BFS
graph = conveyor_to_wall(graph)
if not flag:
    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if type(graph[new_r][new_c]) == tuple:
                tp_r, tp_c = graph[new_r][new_c]
                if graph[tp_r][tp_c] == "." and not cameras[tp_r][tp_c] and distances[tp_r][tp_c] == 10000:
                    q.append((tp_r, tp_c))
                    distances[tp_r][tp_c] = min(distances[tp_r][tp_c], distances[row][col] + 1)
            elif graph[new_r][new_c] == "." and not cameras[new_r][new_c] and distances[new_r][new_c] == 10000:
                q.append((new_r, new_c))
                distances[new_r][new_c] = min(distances[new_r][new_c], distances[row][col] + 1)

# Print the distances for each cell or -1 if unreachable
for r in range(ROWS):
    for c in range(COLS):
        if graph[r][c] == ".":
            print(distances[r][c] if distances[r][c] != 10000 and not flag else -1)
