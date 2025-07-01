import sys

# 读取输入：行数、列数、行回文数、列回文数
ROWS, COLS, rp, cp = map(int, input().split())
rotated = False

# 如果列回文数等于列数或行回文数等于0，交换行和列，并标记旋转
if cp == COLS or rp == 0:
    ROWS, COLS, rp, cp = COLS, ROWS, cp, rp
    rotated = True

# 初始化网格，所有元素初始为'a'
grid = [["a"] * COLS for _ in range(ROWS)]

# 正常情况：创建行和列回文
for i in range(rp):
    grid[i] = ["b"] * COLS
for j in range(cp):
    for i in range(ROWS):
        grid[i][j] = "b"

# 情况1：没有任何回文
if rp == 0 and cp == 0:
    for i in range(ROWS):
        grid[i][0] = "b"
    for j in range(COLS):
        grid[0][j] = "b"
    grid[0][0] = "a"

# 情况2：只有行回文没有列回文
elif cp == 0:
    for i in range(rp, ROWS):
        grid[i][0] = "d"

# 情况3：所有行都是回文，但不是所有列都是回文
if rp == ROWS and cp != COLS:
    remove_col = COLS - cp

    if remove_col % 2 == 1:
        if COLS % 2 == 0:
            print("IMPOSSIBLE")
            sys.exit()
        else:
            for i in range(remove_col // 2):
                grid[0][i] = "c"
                grid[0][COLS - i - 1] = "c"
            grid[0][COLS // 2] = "c"

    else:
        for i in range(remove_col // 2):
            grid[0][i] = "c"
            grid[0][COLS - i - 1] = "c"

# 如果网格被旋转过，将其旋转回原状
if rotated:
    grid = list(zip(*grid))

# 打印网格
for row in grid:
    print(*row, sep="")
