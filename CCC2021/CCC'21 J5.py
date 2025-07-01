# 读取网格的行数和列数
R = int(input())
C = int(input())

# 初始化行和列的颜色状态，初始状态为黑色（False）
rows = [False] * R  # False: 黑色, True: 金色
cols = [False] * C

# 读取查询的数量
queries = int(input())
for _ in range(queries):
    t, i = input().split()
    # 根据查询类型更新行或列的颜色状态
    if t == "R":
        rows[int(i) - 1] = not rows[int(i) - 1]  # 反转颜色状态
    else:
        cols[int(i) - 1] = not cols[int(i) - 1]

# 创建实际的网格，并根据行和列的颜色状态设置单元格颜色
grid = [[False] * C for _ in range(R)]  # 初始化网格为黑色
for r in range(R):
    if rows[r]:
        grid[r] = [True] * C  # 如果行是金色，则设置整行为金色
for c in range(C):
    if cols[c]:
        for r in range(R):
            grid[r][c] = not grid[r][c]  # 反转列中每个单元格的颜色

# 计算并打印金色单元格的总数
print(sum(sum(row) for row in grid))
