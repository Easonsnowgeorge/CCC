# import os
# import sys
# if dict(os.environ).get("is_local", None) == "1":
#     INPUT = open("input.txt", "r")
#     input = lambda: INPUT.readline().strip("\r\n")
# else:
#     input = lambda: sys.stdin.readline().strip("\r\n")
#
# def good(l, r):
#     return 0 <= l < n and 0 <= r < n
#
# n = int(input())
# height = list(map(int, input().split()))
# ans = [float("inf")]*n
#
# if n == 1:
#     print(0)
#     sys.exit()
#
# for i in range(n-1):
#     l = i
#     r = i
#     val = 0
#     while good(l, r):
#         val += abs(height[l] - height[r])
#         ans[r-l] = min(ans[r-l], val)
#         l -= 1
#         r += 1
#     l = i
#     r = i+1
#     val = 0
#     while good(l, r):
#         val += abs(height[l] - height[r])
#         ans[r-l] = min(ans[r-l], val)
#         l -= 1
#         r += 1
# print(*ans)
# TLE

import math

n = int(input())
dp = [[0] * n for _ in range(n)]
a = list(map(int, input().split(" ")))
for len in range(1, n + 1):
    for i in range(0, n - len + 1):
        j = i + len - 1
        if len == 1: continue
        dp[i][j] = dp[i + 1][j - 1] + abs(a[j] - a[i])
ans = [math.inf] * (n + 1)
for len in range(1, n + 1):
    for i in range(0, n - len + 1):
        j = i + len - 1
        ans[len] = min(ans[len], dp[i][j])
for i in range(1, n + 1):
    print(ans[i], end = " ")

