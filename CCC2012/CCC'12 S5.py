ROWS, COLS = map(int, input().split())

# extra array to track cats for simplicity
cats = [[False for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
for i in range(int(input())):  # cats
    r, c = map(int, input().split())
    cats[r][c] = True

# add extra row and col to prevent array out of bounds
dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
dp[1][1] = 1

for r in range(1, ROWS + 1):
    for c in range(1, COLS + 1):
        if not cats[r][c]:
            dp[r][c] += dp[r-1][c] + dp[r][c-1]

print(dp[-1][-1])
