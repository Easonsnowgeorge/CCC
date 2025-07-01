# 读取网格大小
n = int(input())

# 初始化存储树的坐标的列表
trees = []
for _ in range(int(input())):
    r, c = map(int, input().split())
    trees.append((r, c))

# 添加虚拟坐标代表网格的边界
trees.append((0, 0))
trees.append((n + 1, n + 1))

# 按从上到下的顺序对树的坐标进行排序
trees.sort()

# 初始化结果变量
res = 0

# 遍历所有树的坐标
for i in range(len(trees)):
    # 初始化存储水平坐标的列表，包括网格的左右边界
    horizontal = [0, n + 1]

    # 遍历当前树之后的所有树
    for j in range(i + 1, len(trees)):
        # 计算高度（当前树与下一棵树之间的距离减1）
        height = trees[j][0] - trees[i][0] - 1

        # 按从左到右的顺序对水平坐标进行排序
        horizontal.sort()

        # 计算宽度（水平坐标之间的最大距离）
        width = 0
        for k in range(1, len(horizontal)):
            width = max(width, horizontal[k] - horizontal[k - 1] - 1)

        # 更新结果（正方形的边长为高度和宽度中的较小者）
        res = max(res, min(height, width))

        # 将当前树的水平坐标添加到列表中
        horizontal.append(trees[j][1])

# 打印结果
print(res)
