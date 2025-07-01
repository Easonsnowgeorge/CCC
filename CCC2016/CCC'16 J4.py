time = input().split(":")  # 读取时间，并以冒号分隔
time = list(map(int, time))  # 将时间转换为整数列表

n = 120  # 初始化需要行驶的时间（分钟）

# 循环直到完成120分钟的行驶
while n > 0:
    # 判断当前时间是否在高峰时段
    if 7 <= time[0] < 10 or 15 <= time[0] < 19:
        n -= 0.5  # 在高峰时段，每分钟减少0.5分钟的距离
    else:
        n -= 1  # 在非高峰时段，每分钟减少1分钟的距离

    # 增加时间
    time[1] += 1
    if time[1] == 60:
        time[0] += 1
        time[1] = 0
        if time[0] == 24:
            time[0] = 0

# 格式化输出时间
if time[0] < 10:
    time[0] = "0" + str(time[0])
if time[1] < 10:
    time[1] = "0" + str(time[1])

print(f"{time[0]}:{time[1]}")
