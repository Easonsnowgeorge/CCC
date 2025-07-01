n = int(input())  # 读取输入的板块数量
arr = list(map(int, input().split()))  # 读取板块高度数组

count = [0] * 2001  # 初始化一个频率数组，用于记录每个高度板块的数量

# 计算每个高度板块的数量
for i in arr:
    count[i] += 1

res = [0] * 4001  # 初始化一个结果数组，res[i] 表示高度为 i 的篱笆的长度

# 计算每种可能高度的篱笆长度
for i in range(2001):
    for j in range(i, 2001):
        if i == j:  # 如果两块板的高度相同
            res[i + j] += count[i] // 2  # 高度相同的板块只能两两配对
        else:  # 如果两块板的高度不同
            res[i + j] += min(count[i], count[j])  # 高度不同的板块可以任意配对

max_length = max(res)  # 找出最长的篱笆长度
heights = res.count(max_length)  # 计算有多少种不同的高度可以组成这个长度的篱笆
print(max_length, heights)
