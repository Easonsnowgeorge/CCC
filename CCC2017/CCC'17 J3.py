x = input()  # 读取第一个坐标点，格式为字符串
y = input()  # 读取第二个坐标点，格式为字符串
charge = int(input())  # 读取电量，转换为整数

x = x.split()  # 将第一个坐标点分割成列表
y = y.split()  # 将第二个坐标点分割成列表

x1 = int(x[0])  # 提取并转换第一个坐标点的 x 坐标
y1 = int(y[0])  # 提取并转换第二个坐标点的 x 坐标
x2 = int(x[1])  # 提取并转换第一个坐标点的 y 坐标
y2 = int(y[1])  # 提取并转换第二个坐标点的 y 坐标

run = x1 - y1  # 计算 x 坐标之差
rise = x2 - y2  # 计算 y 坐标之差

# 如果 run 是负数，则移除负号并转换回整数
if str(run)[0] == "-":
    run = str(run)
    run = run.replace("-", "")
    run = int(run)

# 如果 rise 是负数，则移除负号并转换回整数
if str(rise)[0] == "-":
    rise = str(rise)
    rise = rise.replace("-", "")
    rise = int(rise)

total = rise + run  # 计算总移动距离

# 如果电量和总移动距离的奇偶性相同且电量足够，则输出 "Y"，否则输出 "N"
if (charge%2 == total%2) and charge >= total:
    print("Y")
else:
    print("N")
