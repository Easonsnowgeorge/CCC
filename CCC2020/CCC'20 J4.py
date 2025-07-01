# 读取要搜索的文本
text = input()
# 读取要查找的字符串，并转换为列表以便进行循环置换
to_find = list(input())

# 初始化输出为"no"
printing = "no"

# 遍历to_find的长度次，检查所有可能的循环置换
for _ in range(len(to_find)):
    # 将列表的第一个元素移动到最后
    temp = to_find[0]
    del to_find[0]
    to_find.append(temp)

    # 将循环置换后的列表转换回字符串
    to_find_string = ''.join(to_find)

    # 检查循环置换后的字符串是否存在于text中
    if to_find_string in text:
        printing = "yes"
        break

# 打印结果
print(printing)
