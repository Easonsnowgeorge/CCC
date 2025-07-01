# 读取测量值的数量
n = int(input())

# 读取每个测量值的时间和位置，并存储在列表中
measurements = [list(map(int, input().split())) for _ in range(n)]  # (time, location)

# 根据时间对测量值进行排序
measurements.sort()  # sort based on time

# 初始化最大速度为0
max_speed = 0

# 遍历所有测量值
for i in range(1, n):
    # 计算两个连续测量值之间的时间差
    time = measurements[i][0] - measurements[i - 1][0]
    # 计算两个连续测量值之间的位置差
    distance = abs(measurements[i][1] - measurements[i - 1][1])
    # 计算速度
    speed = distance / time
    # 更新最大速度
    max_speed = max(max_speed, speed)

# 打印最大速度
print(max_speed)
