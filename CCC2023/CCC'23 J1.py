# 读取用户输入的包裹数量
packages = int(input())

# 读取用户输入的碰撞次数
collisions = int(input())

# 初始化得分为0
point = 0

# 如果包裹数量大于碰撞次数，给额外的得分
if packages > collisions:
    point += 500

# 计算最终得分：每个包裹加50分，每次碰撞减10分，加上额外得分
print(packages * 50 - collisions * 10 + point)
