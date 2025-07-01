# def apply_rule(rule, sequence, start):
#     # 替换规则应用于序列的指定位置
#     return sequence[:start] + rule[1] + sequence[start + len(rule[0]):]
#
# def find_sequence(rules, current_sequence, final_sequence, steps, path):
#     if steps == 0:
#         # 如果已经达到指定步数，检查当前序列是否与最终序列匹配
#         return current_sequence == final_sequence, path
#
#     for i, rule in enumerate(rules):
#         for pos in range(len(current_sequence) - len(rule[0]) + 1):
#             # 对每个规则的每个可能位置应用规则
#             if current_sequence[pos:pos + len(rule[0])] == rule[0]:
#                 new_sequence = apply_rule(rule, current_sequence, pos)
#                 found, new_path = find_sequence(rules, new_sequence, final_sequence, steps - 1, path + [(i + 1, pos + 1, new_sequence)])
#                 if found:
#                     return True, new_path
#
#     return False, path
#
# # 读取替换规则
# rules = [input().split() for _ in range(3)]
#
# # 读取步数、初始序列和最终序列
# steps, initial_sequence, final_sequence = input().split()
# steps = int(steps)
#
# # 寻找替换序列
# found, sequence = find_sequence(rules, initial_sequence, final_sequence, steps, [])
#
# # 打印结果
# if found:
#     for step in sequence:
#         print(*step)
# else:
#     print("No solution found")





# from collections import deque
#
# def apply_rule(rule, sequence, start):
#     return sequence[:start] + rule[1] + sequence[start + len(rule[0]):]
#
# def bfs(rules, initial_sequence, final_sequence, steps):
#     queue = deque([(initial_sequence, [], 0)])  # (当前序列, 替换路径, 步数)
#
#     while queue:
#         current_sequence, path, current_steps = queue.popleft()
#
#         if current_steps == steps:
#             if current_sequence == final_sequence:
#                 return path
#             continue
#
#         for i, rule in enumerate(rules):
#             for pos in range(len(current_sequence) - len(rule[0]) + 1):
#                 if current_sequence[pos:pos + len(rule[0])] == rule[0]:
#                     new_sequence = apply_rule(rule, current_sequence, pos)
#                     new_path = path + [(i + 1, pos + 1, new_sequence)]
#                     queue.append((new_sequence, new_path, current_steps + 1))
#
#     return None
#
# # 读取替换规则
# rules = [input().split() for _ in range(3)]
#
# # 读取步数、初始序列和最终序列
# steps, initial_sequence, final_sequence = input().split()
# steps = int(steps)
#
# # 使用 BFS 寻找替换序列
# path = bfs(rules, initial_sequence, final_sequence, steps)
#
# # 打印结果
# if path:
#     for step in path:
#         print(*step)
# else:
#     print("No solution found")



# def apply_rule(rule, sequence, start):
#     return sequence[:start] + rule[1] + sequence[start + len(rule[0]):]
#
# def dp(rules, initial_sequence, final_sequence, steps):
#     # 创建一个字典来存储每个序列及其路径
#     dp_dict = {initial_sequence: []}
#
#     for step in range(steps):
#         new_dp_dict = {}
#         for seq, path in dp_dict.items():
#             for i, rule in enumerate(rules):
#                 for pos in range(len(seq) - len(rule[0]) + 1):
#                     if seq[pos:pos + len(rule[0])] == rule[0]:
#                         new_seq = apply_rule(rule, seq, pos)
#                         new_path = path + [(i + 1, pos + 1, new_seq)]
#                         if new_seq not in new_dp_dict or len(new_dp_dict[new_seq]) > len(new_path):
#                             new_dp_dict[new_seq] = new_path
#         dp_dict = new_dp_dict
#
#     return dp_dict.get(final_sequence)
#
# # 读取替换规则
# rules = [input().split() for _ in range(3)]
#
# # 读取步数、初始序列和最终序列
# steps, initial_sequence, final_sequence = input().split()
# steps = int(steps)
#
# # 使用 DP 寻找替换序列
# path = dp(rules, initial_sequence, final_sequence, steps)
#
# # 打印结果
# if path:
#     for step in path:
#         print(*step)
# else:
#     print("No solution found")

def apply_rule(rule, sequence, start):
    return sequence[:start] + rule[1] + sequence[start + len(rule[0]):]

def dfs(rules, current_sequence, final_sequence, steps, cache, path):
    if steps < 0:
        return False
    if current_sequence == final_sequence:
        return True
    if (current_sequence, steps) in cache and cache[(current_sequence, steps)] == False:
        return False

    for i, rule in enumerate(rules):
        for pos in range(len(current_sequence) - len(rule[0]) + 1):
            if current_sequence[pos:pos + len(rule[0])] == rule[0]:
                new_sequence = apply_rule(rule, current_sequence, pos)
                if dfs(rules, new_sequence, final_sequence, steps - 1, cache, path):
                    path.append((i + 1, pos + 1, new_sequence))
                    return True

    cache[(current_sequence, steps)] = False
    return False

# 读取替换规则
rules = [input().split() for _ in range(3)]

# 读取步数、初始序列和最终序列
steps, initial_sequence, final_sequence = input().split()
steps = int(steps)

# 使用记忆化搜索
cache = {}
path = []
if dfs(rules, initial_sequence, final_sequence, steps, cache, path):
    for step in reversed(path):
        print(*step)
else:
    print("No solution found")

