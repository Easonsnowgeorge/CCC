# 读取数字n，代表数据行中的元素数量
n = int(input())

# 读取第一行的数据，转换为整数列表，并在列表前添加一个0
row1 = [0] + list(map(int, input().split()))

# 读取第二行的数据，转换为整数列表，并在列表前添加一个0
row2 = [0] + list(map(int, input().split()))

# 初始化总分为0
total = 0

# 遍历第一行的每个元素
for i in range(1, n + 1):
    # 如果当前元素为1
    if row1[i] == 1:
        # 如果前一个元素也为1，总分加1
        if row1[i - 1] == 1:
            total += 1
        else:
            # 否则，总分加3
            total += 3

# 遍历第二行的每个元素
for i in range(1, n + 1):
    # 如果当前元素为1
    if row2[i] == 1:
        # 总分先加3
        total += 3
        # 如果前一个元素也为1，总分减2
        if row2[i - 1] == 1:
            total -= 2
        # 如果当前索引是奇数并且第一行对应的元素为1，总分再减2
        if i % 2 == 1 and row1[i] == 1:
            total -= 2

# 打印最终的总分
print(total)
