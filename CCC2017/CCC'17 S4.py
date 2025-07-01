import sys

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

# 读取输入的节点数、边数和 pipe enhancer 的值
n, m, d = map(int, input().split())
edges = []
current = []  # 当前的计划
for i in range(m):
    pipe = tuple(map(int, input().split()))
    if i < n - 1:
        current.append(pipe)
    edges.append(pipe)

edges.sort(key=lambda x: x[2])  # 根据成本排序
uf = UnionFind(n + 1)
mst = []

# 构建最小生成树
for n1, n2, cost in edges:
    if len(mst) == n - 1:  # 如果最小生成树已完成
        break
    if uf.find(n1) != uf.find(n2):
        uf.union(n1, n2)
        mst.append((n1, n2, cost))

# 计算切换到最小生成树所需的时间
mst_set, original_set = set(mst), set(current)
no_pipe = len(mst_set - original_set)
if d == 0:
    print(no_pipe)
    sys.exit()

# 考虑 pipe enhancer 的情况下重新构建最小生成树
mst_max_cost = mst[-1][2]
uf = UnionFind(n + 1)
mst = []

for n1, n2, cost in edges:
    if len(mst) == n - 1:
        break
    if uf.find(n1) != uf.find(n2):
        if cost < mst_max_cost or (cost == mst_max_cost and (n1, n2, cost) in original_set):
            uf.union(n1, n2)
            mst.append((n1, n2, cost))
        elif cost <= d and (n1, n2, cost) in original_set:
            print(no_pipe - 1)
            sys.exit()

print(no_pipe)
