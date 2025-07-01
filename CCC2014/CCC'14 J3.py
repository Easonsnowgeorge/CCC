times = int(input())  # 读取比赛次数

p1 = 100  # 初始化玩家p1的分数
p2 = 100  # 初始化玩家p2的分数

i = 0
while i < times:  # 循环处理每次比赛
    x = input().split(None, 1)  # 读取每次比赛的骰子点数

    if int(x[0]) > int(x[1]):  # 如果p1的骰子点数高于p2
        p2 -= int(x[0])  # p2失去p1骰子点数的分数
    elif int(x[1]) > int(x[0]):  # 如果p2的骰子点数高于p1
        p1 -= int(x[1])  # p1失去p2骰子点数的分数

    i += 1

print(p1)  # 输出p1的最终分数
print(p2)  # 输出p2的最终分数
