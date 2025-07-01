# 读取坐标点的数量
items = int(input())

# 初始化最小和最大x、y坐标值
min_x = 100
max_x = 0
min_y = 100
max_y = 0

# 初始化计数器
i = 0
while i < items:
    # 读取坐标点
    x = input()
    coords = x.split(",")
    # 更新最小和最大x坐标值
    if int(coords[0]) < min_x:
        min_x = int(coords[0])
    if int(coords[0]) > max_x:
        max_x = int(coords[0])
    # 更新最小和最大y坐标值
    if int(coords[1]) < min_y:
        min_y = int(coords[1])
    if int(coords[1]) > max_y:
        max_y = int(coords[1])

    i += 1

# 打印最小外围矩形的左下角和右上角坐标
print(f"{min_x-1},{min_y-1}")
print(f"{max_x+1},{max_y+1}")
