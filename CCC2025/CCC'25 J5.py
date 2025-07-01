def min_cost_path(rows, cols, m, grid):
    """
    使用动态规划计算最小成本路径。

    Args:
        rows: 网格的行数。
        cols: 网格的列数。
        m: 瓷砖成本的最大值。
        grid: 网格的二维数组。

    Returns:
        最小成本路径的成本。
    """
    [print]

    # 创建 dp 数组
    dp = [[float('inf')] * cols for _ in range(rows)]

    # 初始化第一行
    for j in range(cols):
        dp[0][j] = grid[0][j]

    # 计算其他行的最小成本
    for i in range(1, rows):
        for j in range(cols):
            # 计算当前瓷砖的成本
            cost = grid[i][j]

            # 计算相邻瓷砖的最小成本
            prev_costs = []
            if j > 0:
                prev_costs.append(dp[i - 1][j - 1])
            prev_costs.append(dp[i - 1][j])
            if j < cols - 1:
                prev_costs.append(dp[i - 1][j + 1])

            # 更新 dp 数组
            dp[i][j] = cost + min(prev_costs)

    # 找到最后一行中的最小成本
    return min(dp[rows - 1])

# 示例输入
rows = int(input())
cols = int(input())
m = int(input())
grid = []
# 填充网格 从1开始 到m结束
for i in range(rows):
    row = []
    for j in range(cols):
        cost = ((i)*cols+ (j + 1))%m
        if cost == 0:
            row.append(m)
        else:
            row.append(cost)
    grid.append(row)
# print(grid)
# 计算最小成本路径
min_cost = min_cost_path(rows, cols, m, grid)

# 输出结果
print(min_cost)