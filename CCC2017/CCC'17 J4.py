n = int(input())  # 读取时间，转换为整数
time = [1, 2, 0, 0]  # 初始化时间为 12:00
count = 0  # 初始化特殊时间的计数

# 如果时间大于720分钟（一个完整的时钟周期），则计算可以整除的周期数量，并相应增加计数
if n > 720:
    count += (n // 720) * 31  # 每个周期内有31个特殊时间
    n %= 720  # 计算剩余的时间

for i in range(n):
    # 逐分钟增加时间
    time[3] += 1
    if time[3] > 9:
        time[3] = 0
        time[2] += 1
    if time[2] == 6 and time[3] == 0:
        time[2] = 0
        time[1] += 1
    if time[1] > 9:
        time[1] = 0
        time[0] += 1
    if time[0] == 1 and time[1] > 2:
        time = [0, 1, 0, 0]  # 调整时间到下一个小时

    # 检查时间是否为特殊时间
    temp = time.copy()

    difference = temp[2] - temp[3]  # 计算最后两位数字的差
    for j in range(len(temp) - 1):
        special = True
        if j == 0 and temp[j] == 0:
            continue
        if temp[j] - temp[j + 1] != difference:  # 检查是否所有数字都符合等差数列
            special = False
            break

    if special:
        count += 1
        special = False

print(count)
