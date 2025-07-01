import sys
from heapq import heappush, heappop, heapify
from collections import deque


class Multiset:
    def __init__(self, arr=None):
        """Create multiset from list"""
        if arr is None:
            arr = []
        self.heap = arr  # keeps track of smallest element, with lazy removal (not real time, only update when removing)
        heapify(self.heap)
        self.freq = {}  # keeps track of the actual elements in real time
        for i in arr:
            if i not in self.freq:
                self.freq[i] = 0
            self.freq[i] += 1

    def add(self, val) -> None:
        """Add an element to the multiset"""
        heappush(self.heap, val)

        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1

    def remove(self, val) -> None:
        """Remove an element from multiset by value"""
        if val not in self.freq:
            raise Exception("Cannot remove from empty multiset") from ValueError

        self.freq[val] -= 1
        if self.freq[val] == 0:  # remove useless keys
            del self.freq[val]

    def discard(self, val) -> bool:
        """Remove an element from multiset by value without raising error is the element doesn't exist"""
        if val not in self.freq:
            return False
        self.remove(val)
        return True

    def smallest(self):
        """Get the smallest element in the multiset"""
        while self.heap:
            el = self.heap[0]
            if el in self.freq:
                return el
            heappop(self.heap)  # lazy remove
        raise Exception("Cannot get smallest element from empty multiset") from ValueError

    def pop(self):
        """Removes and returns the smallest element in the multiset"""
        while self.heap:
            el = heappop(self.heap)
            if el in self.freq:
                self.freq[el] -= 1  # update frequency
                if self.freq[el] == 0:
                    del self.freq[el]
                return el
        raise Exception("Cannot pop from empty multiset") from ValueError

    def count(self, val) -> int:
        if val in self.freq:
            return self.freq[val]
        return 0

    def __bool__(self):
        return len(self.freq) != 0

    def __contains__(self, item):
        return item in self.freq

    def __str__(self):
        res = []
        for el, cnt in self.freq.items():
            res.extend([el] * cnt)
        return str(res)


input = sys.stdin.readline
N, M, D = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # reverse graph

route = list(map(int, input().split()))

dist = [1 << 30] * (N + 1)
dist[N] = 0
q = deque([(0, N)])  # dist, current node

while q:  # BFS to get distance from all nodes to N
    d, cur = q.popleft()
    for adj in graph[cur]:
        new_d = d + 1
        if dist[adj] > new_d:  # found shorter path, update distance
            dist[adj] = new_d
            q.append((new_d, adj))

options = Multiset([dist[v] + i for i, v in enumerate(route)])  # compute all possible (routes + train)

for _ in range(D):
    a, b = map(lambda x: int(x) - 1, input().split())

    options.add(dist[route[a]] + b)  # update distances caused by train swapping
    options.add(dist[route[b]] + a)
    options.discard(dist[route[a]] + a)
    options.discard(dist[route[b]] + b)

    route[a], route[b] = route[b], route[a]
    print(options.smallest())
