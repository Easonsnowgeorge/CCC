# 初始化输出列表
output = []

# 初始化用于存储上一个有效方向的变量
previous = ""

# 循环读取输入直到输入为"99999"
while True:
    code = str(input())

    # 检测终止条件
    if code == "99999":
        break

    # 将代码转换为字符列表
    x = list(code)

    # 如果前两位数字之和为0，则使用上一个有效方向
    if int(x[0]) + int(x[1]) == 0:
        output.append(f"{previous} {x[2]}{x[3]}{x[4]}")

    # 如果前两位数字之和为偶数，则方向为"right"
    elif (int(x[0]) + int(x[1])) % 2 == 0:
        output.append(f"right {x[2]}{x[3]}{x[4]}")
        previous = "right"

    # 如果前两位数字之和为奇数，则方向为"left"
    else:
        output.append(f"left {x[2]}{x[3]}{x[4]}")
        previous = "left"

# 打印所有输出
for i in output:
    print(i)
