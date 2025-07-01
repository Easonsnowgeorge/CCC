from collections import defaultdict

# 初始化“相同”关系的字典
same = defaultdict(set)
for _ in range(int(input())):
    a, b = input().split()
    same[a].add(b)

# 初始化“不同”关系的字典
different = defaultdict(set)
for _ in range(int(input())):
    a, b = input().split()
    different[a].add(b)

res = 0  # 初始化结果变量

# 处理每个查询
for _ in range(int(input())):
    abc = input().split()  # 读取查询中的元素
    for x in abc:
        to_remove = set()
        # 检查“相同”关系是否被违反
        for s in same[x]:
            if s not in abc:
                to_remove.add(s)
                res += 1
        same[x] -= to_remove  # 从关系集合中移除违反的关系

        to_remove = set()
        # 检查“不同”关系是否被违反
        for p in abc:
            if p != x and p in different[x]:
                to_remove.add(p)
                res += 1
        different[x] -= to_remove  # 从关系集合中移除违反的关系

print(res)  # 输出违反的次数
