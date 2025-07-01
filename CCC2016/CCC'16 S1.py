from collections import Counter

s1 = Counter(input())  # 读取第一个字符串，并统计每个字符的出现次数
s2 = Counter(input())  # 读取第二个字符串，并统计每个字符的出现次数

diff = 0  # 初始化差值变量
res = 0  # 初始化结果变量，表示需要替换的字符数量
for char, count in s1.items():
    diff = count - s2[char]  # 计算每个字符在 s1 和 s2 中的差值
    if diff < 0:  # 如果 s1 中的字符比 s2 中的字符少
        res = float('inf')  # 无法通过替换使 s2 变为 s1
    else:
        res += diff  # 累加需要替换的字符数量

# 输出结果
# 如果需要替换的字符数量小于等于 s2 中通配符的数量，则输出 "A"，否则输出 "N"
print("A" if res <= s2["*"] else "N")
