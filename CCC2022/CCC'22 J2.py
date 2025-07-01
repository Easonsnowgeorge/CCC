# 读取用户要输入的球队数量
repeats = int(input())

# 初始化获得金牌的球队数量为0
golds = 0

# 初始化一个标志，表示是否所有球队都获得了金牌
gold_team = True

# 初始化一个计数器
i = 0

# 循环读取每个球队的得分和犯规次数
while repeats > i:
    points = int(input())  # 读取得分
    foul = int(input())    # 读取犯规次数

    # 计算总分
    total = points * 5 - foul * 3

    # 如果总分超过40，增加金牌数量
    if total > 40:
        golds += 1
    else:
        # 否则，设置标志为False，表示不是所有球队都获得了金牌
        gold_team = False

    i += 1

# 打印获得金牌的球队数量
print(golds, end="")

# 如果所有球队都获得了金牌，打印加号
if gold_team == True:
    print("+")
