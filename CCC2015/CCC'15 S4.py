import sys
import heapq

input = sys.stdin.readline
hull, n_islands, n_routes = map(int, input().split())  # 读取船只耐久度、岛屿数量和航线数量
graph = [[] for _ in range(n_islands + 1)]  # 初始化图的邻接表

# 读取每条航线的信息并构建图
for _ in range(n_routes):
    a, b, pt, dmg = map(int, input().split())
    graph[a].append((b, pt, dmg))
    graph[b].append((a, pt, dmg))

start, end = map(int, input().split())  # 读取起点和终点

inf = 10 ** 9 + 1
dist = [[inf]*201 for _ in range(n_islands + 1)]  # 初始化距离数组，考虑耐久度
for i in range(201):
    dist[start][i] = 0  # 起点到自己的距离总是0

pq = [(0, start, 0)]  # 优先队列，存储(距离, 岛屿, 损害)

# 进行 Dijkstra 算法的搜索
while pq:
    time, island, damage = heapq.heappop(pq)
    if island == end:  # 如果到达终点，打印时间并退出
        print(time)
        sys.exit()

    # 检查所有邻接的岛屿
    for adj, adj_time, adj_damage in graph[island]:
        new_time = time + adj_time
        new_damage = damage + adj_damage

        if new_damage >= hull:  # 如果耐久度耗尽，跳过此路径
            continue

        if new_time < dist[adj][new_damage]:  # 如果找到更短的路径
            dist[adj][new_damage] = new_time
            heapq.heappush(pq, (new_time, adj, new_damage))

print(-1)  # 如果无法到达终点，打印-1
