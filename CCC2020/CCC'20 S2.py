import sys
from collections import deque

ROWS = int(input())  # 读取行数
COLS = int(input())  # 读取列数
end = ROWS * COLS  # 计算终点的值
graph = [[] for _ in range(end + 1)]  # 初始化图的邻接表

# 构建图
for r in range(1, ROWS + 1):
    row = map(int, input().split())  # 读取每行的整数
    c = 1
    for num in row:
        if num <= end:
            graph[r * c].append(num)  # 将每个整数视为图中的一个节点
        c += 1

# 使用 BFS 在邻接表上进行搜索
visited = [False for _ in range(end + 1)]  # 初始化访问状态数组
visited[1] = True  # 标记起点为已访问
q = deque([1])  # 初始化队列，从起点开始

while q:
    current = q.popleft()  # 弹出当前节点

    if current == end:  # 检查是否到达终点
        print("yes")
        sys.exit()  # 结束程序

    for adj in graph[current]:
        if not visited[adj]:  # 检查邻接节点是否已访问
            visited[adj] = True
            q.append(adj)  # 将未访问的邻接节点加入队列

print("no")  # 如果没有找到路径，输出"no"
