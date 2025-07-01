N, M = map(int, input().split())  # 读取节点总数 N 和关键节点数量 M
pho = set(map(int, input().split()))  # 读取关键节点集合

graph = [set() for _ in range(N)]  # 创建图的邻接表表示
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)  # 构建无向图

# 修剪树的叶子节点，直到到达关键节点或分支的末端
for node in range(N):
    while len(graph[node]) == 1 and node not in pho:
        prev = node
        node = list(graph[node])[0]
        graph[prev].remove(node)  # 移除连接，叶子节点移动到下一个节点
        graph[node].remove(prev)

def farthest(start):
    dist = [-1] * N
    dist[start] = 0
    stack = [(start, -1)]
    while stack:
        cur, prev = stack.pop()
        for adj in graph[cur]:
            if adj != prev:
                stack.append((adj, cur))
                dist[adj] = dist[cur] + 1
    far = max(dist)
    return far, dist.index(far)  # 返回从start开始的最大距离和最远节点

# 获取树的直径，从一个关键节点开始，因为我们知道它没有被修剪
_, end1 = farthest(list(pho)[0])
diameter, end2 = farthest(end1)

node_count = sum(len(u) != 0 for u in graph)  # 修剪后树中的节点数量
total = (node_count - 1) * 2  # 遍历所有节点的总长度，每条边恰好被走两次

# 由于不需要回到起点，可以通过直径的边只走一次来节省时间
print(total - diameter)
