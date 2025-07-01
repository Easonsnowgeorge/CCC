arr = []

# 读取并构建一个 4x4 矩阵
for i in range(4):
    x = input().split()
    arr.append(list(map(int, x)))

# 初始化 value 为第一行的和
value = sum(arr[0])
flag = True

# 检查每行的和是否与第一行的和相等
for i in arr:
    if sum(i) != value:
        flag = False
        break

# 如果每行的和相等，则继续检查每列的和
if flag:
    total = 0
    for j in range(4):
        total = 0
        for k in range(4):
            total += arr[k][j]

        if total != value:
            flag = False
            break

# 输出结果
if flag:
    print("magic")
else:
    print("not magic")
