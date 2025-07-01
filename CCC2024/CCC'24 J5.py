from collections import deque


def calculate_harvest_value(rows, cols, patch, start_row, start_col):
    # Map pumpkin sizes to their values
    values = {'S': 1, 'M': 5, 'L': 10}

    # Initialize BFS
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    total_value = 0

    # Directions for movement (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Perform BFS
    while queue:
        row, col = queue.popleft()
        if patch[row][col] in values:
            total_value += values[patch[row][col]]

        for drow, dcol in directions:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < rows and 0 <= ncol < cols and not visited[nrow][ncol] and patch[nrow][ncol] != '*':
                visited[nrow][ncol] = True
                queue.append((nrow, ncol))

    return total_value


# Example usage
rows = int(input())
cols = int(input())
patch = [input() for _ in range(rows)]
start_row = int(input())
start_col = int(input())

# Calculate the total value
total_value = calculate_harvest_value(rows, cols, patch, start_row, start_col)
print(total_value)
