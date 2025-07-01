# 读取用户将要输入的记录数量
times = int(input())

# 初始化记录最高金额的名称和金额
highest = ""
highest_number = 0

# 初始化计数器
time = 0
while time < times:
    # 读取每条记录的名称和金额
    name = input()
    amount = int(input())

    # 如果当前记录的金额高于之前记录的最高金额，则更新最高金额和对应的名称
    if amount > highest_number:
        highest = name
        highest_number = amount

    # 更新计数器
    time += 1

# 打印金额最高的记录的名称
print(highest)
