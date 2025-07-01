from itertools import accumulate

n = int(input())  # 读取轮数
team1 = list(map(int, input().split()))  # 读取队伍1的得分数组
team2 = list(map(int, input().split()))  # 读取队伍2的得分数组

team1 = list(accumulate(team1))  # 计算队伍1的得分累计
team2 = list(accumulate(team2))  # 计算队伍2的得分累计

res = 0  # 初始化结果变量
for i in reversed(range(n)):  # 从后向前遍历数组
    if team1[i] == team2[i]:  # 检查两个队伍的得分是否相同
        res = i+1  # 如果相同，记录这个位置（加1是因为索引从0开始）
        break

print(res)  # 输出结果
