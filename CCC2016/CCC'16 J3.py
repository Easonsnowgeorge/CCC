def manacher(s):
    t = '#'.join('^{}$'.format(s))  # 将原字符串s转换为新字符串t，每个字符之间插入'#'，并在两端添加'^'和'$'
    n = len(t)  # t的长度
    p = [0] * n  # p数组用于存储以每个字符为中心的最长回文半径
    c = r = 0  # c是当前找到的最长回文的中心位置，r是这个回文的右边界

    for i in range(1, n-1):
        if r > i:
            p[i] = min(r - i, p[2*c - i])  # 利用之前的回文信息来初始化p[i]
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1  # 扩展当前中心的回文长度
        if i + p[i] > r:
            c, r = i, i + p[i]  # 更新最长回文的中心和右边界

    max_len, center_index = max((p[i], i) for i in range(1, n-1))  # 找到最长的回文半径和对应的中心位置
    start_index = (center_index - max_len) // 2  # 计算原字符串中回文开始的位置
    return len(s[start_index: start_index + max_len])  # 返回最长回文的长度

print(manacher(input()))  # 读取输入字符串并打印最长回文子串的长度
