t = int(input())  # 读取操作类型（1或2）
n = int(input())  # 读取成员数量
dmoj = sorted(list(map(int, input().split())))  # 读取并排序DMOJ团队成员的能力值
peg = sorted(list(map(int, input().split())))  # 读取并排序PEG团队成员的能力值

if t == 1:
    pairs = list(zip(dmoj, peg))  # 如果操作类型为1，直接配对两组数
    print(sum([max(i) for i in pairs]))  # 计算每对中的最大值，然后求和
else:
    peg.reverse()  # 如果操作类型为2，将PEG团队成员的能力值反转（降序排序）
    pairs = list(zip(dmoj, peg))  # 配对两组数
    print(sum([max(i) for i in pairs]))  # 计算每对中的最大值，然后求和
