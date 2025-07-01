N = int(input())  # 读取球的数量
dp = [[0 for _ in range(402)] for _ in range(402)]  # 初始化动态规划数组
total = [0 for _ in range(402)]  # 初始化前缀和数组

res = 0  # 初始化结果变量
balls = list(map(int, input().split()))  # 读取每个球的分数值
for i in range(N):
    dp[i][i] = balls[i]  # 单个球的分数
    res = max(res, dp[i][i])  # 更新最大分数
    if i == 0:
        total[0] = dp[i][i]
    else:
        total[i] = total[i - 1] + dp[i][i]  # 计算前缀和

# 遍历所有可能的子区间
for length in range(1, N):
    for l in range(N - length):
        r = l + length
        j = l + 1
        k = r
        # 尝试合并球并更新dp[l][r]
        while j <= k:
            if dp[l][j - 1] and dp[l][j - 1] == dp[k][r] and (j == k or dp[j][k - 1]):
                dp[l][r] = max(dp[l][r], dp[l][j - 1] + dp[j][k - 1] + dp[k][r])
                res = max(res, dp[l][r])
                break
            if total[j - 1] - total[l - 1] < total[r] - total[k - 1]:
                j += 1
            else:
                k -= 1

print(res)
