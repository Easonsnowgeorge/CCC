from sys import stdin
input = stdin.readline

N = int(input())  # 读取矩形的数量
T = int(input())  # 读取染色强度阈值
px = set()  # 存储所有矩形的x坐标
py = set()  # 存储所有矩形的y坐标
rects = []  # 存储所有矩形的信息

# 读取每个矩形的信息
for i in range(N):
    x1, y1, x2, y2, t = map(int, input().split())
    px.add(x1)
    px.add(x2)
    py.add(y1)
    py.add(y2)
    rects.append([x1, y1, x2, y2, t])

# 压缩坐标，减小数组大小
px = sorted(list(px))
py = sorted(list(py))
cx = {px[i - 1]: i for i in range(1, len(px) + 1)}
cy = {py[i - 1]: i for i in range(1, len(py) + 1)}

# 初始化差分数组
diff = [[0] * (len(px) + 1) for i in range(len(py) + 1)]

# 填充差分数组
for i in range(N):
    x1, y1, x2, y2, t = rects[i]
    x1, y1, x2, y2 = cx[x1], cy[y1], cx[x2], cy[y2]
    diff[y1][x1] += t
    diff[y2][x2] += t
    diff[y1][x2] -= t
    diff[y2][x1] -= t

# 计算染色强度满足阈值的区域面积
res = 0
for i in range(1, len(py) + 1):
    for j in range(1, len(px) + 1):
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        if diff[i][j] >= T:
            res += (py[i] - py[i - 1]) * (px[j] - px[j - 1])

print(res)  # 输出结果
