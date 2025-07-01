length = int(input())  # 读取列表长度
a = input().split()  # 读取第一组字符串
b = input().split()  # 读取第二组字符串

groups = {}  # 初始化用于存储配对关系的字典
result = "good"  # 初始化结果

# 遍历两个列表，检查配对是否有效
for i in range(length):
    if a[i] == b[i]:  # 如果一个字符串与自身配对
        result = "bad"
        break
    if a[i] in groups or b[i] in groups:  # 如果字符串已经出现在其他配对中
        if a[i] in groups.keys():
            if groups[a[i]] != b[i]:  # 检查配对是否一致
                result = "bad"
                break
        elif b[i] in groups.keys():
            if groups[b[i]] != a[i]:  # 检查配对是否一致
                result = "bad"
                break
    else:
        groups[a[i]] = b[i]  # 建立新的配对关系

print(result)  # 输出结果
