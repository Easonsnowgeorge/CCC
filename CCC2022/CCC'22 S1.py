# 读取用户输入的数字
num = int(input())

# 初始化计数器为0
count = 0

# 检查数字是否能被5整除
if num % 5 == 0:
    count += 1

# 循环直到数字小于等于0
while num > 0:
    # 检查数字是否能被4整除
    if num % 4 == 0:
        count += 1
    # 每次循环减去5
    num -= 5

# 打印计数器的值
print(count)
