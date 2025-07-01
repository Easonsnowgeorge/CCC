from math import lcm, gcd
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 读取数组大小和查询数量
queries = [tuple(map(int, input().split())) for _ in range(M)]  # 读取查询

# 初始化差分数组
diff = [[0] * (N + 2) for _ in range(17)]  # 1到16的GCD，加上额外的填充
for i, j, x in queries:
    diff[x][i] += 1
    diff[x][j + 1] -= 1

# 使用最小公倍数构造输出数组
res = [0] * N
for i in range(1, N + 1):
    cur = 1
    for z in range(17):
        diff[z][i] += diff[z][i - 1]
        if diff[z][i] != 0:
            cur = lcm(cur, z)  # 使用最小公倍数更新当前值
    res[i - 1] = cur

# 使用稀疏表快速检查查询的GCD是否正确
bits = N.bit_length()  # log2
st = [[0] * bits for _ in range(N)]
for i in range(N):
    st[i][0] = res[i]

for k in range(1, bits):
    for i in range(N - (1 << k) + 1):
        st[i][k] = gcd(st[i][k - 1], st[i + (1 << (k - 1))][k - 1])

# 检查查询是否满足条件
for l, r, x in queries:
    l -= 1  # 0索引
    r -= 1
    k = (r - l + 1).bit_length() - 1
    if gcd(st[l][k], st[r - (1 << k) + 1][k]) != x:
        print("Impossible")
        sys.exit()

print(*res)
