from bisect import bisect_right

gates = [i for i in range(1, int(input()) + 1)]  # 初始化所有可用登机口的列表
n = int(input())  # 读取飞机的数量

res = 0
for _ in range(n):
    plane = int(input())  # 读取每架飞机的最大登机口号
    curr = bisect_right(gates, plane)  # 找到这架飞机可以占据的最大可能登机口
    if curr == 0:  # 如果没有合适的登机口，则停止
        break
    else:
        res += 1
        gates.pop(curr - 1)  # 移除该登机口，因为当前飞机已经占据

print(res)  # 输出成功降落的飞机数量
