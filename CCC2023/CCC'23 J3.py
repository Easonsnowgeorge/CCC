# 读取天数
days = int(input())

# 初始化一个列表来存储每天的出勤数据
db = []

# 循环读取每一天的出勤情况，并添加到列表中
for i in range(days):
    people = list(input())
    db.append(people)

# 转置出勤数据列表，使其每一列代表一天的出勤情况
db = list(zip(*db))

# 初始化一个列表来存储每天出勤人数（即'Y'的数量）
yeses = []

# 计算每一列（即每一天）中'Y'的数量，并添加到列表中
for i in range(len(db)):
    yes = db[i].count("Y")
    yeses.append(yes)

# 找出出勤人数最多的数量
most = max(yeses)

# 初始化一个列表来存储出勤人数最多的天数
out = []

# 遍历每天的出勤人数，如果等于最多的数量，则添加这一天到列表中
for i, day in enumerate(yeses, start=1):
    if day == most:
        out.append(i)

# 打印出勤人数最多的天数，天数之间用逗号分隔，最后一个天数后没有逗号
for i in range(len(out)-1):
    print(out[i], end=",")

print(out[-1], end="")
