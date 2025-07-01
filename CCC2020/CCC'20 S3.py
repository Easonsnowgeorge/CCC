import sys

needle = input()  # 读取 needle 字符串
ln = len(needle)
letters = [0] * 26  # 初始化 needle 字符串的字母频率数组
for char in needle:
    letters[ord(char) - 97] += 1

haystack = input()  # 读取 haystack 字符串
lh = len(haystack)

# 如果 needle 字符串长于 haystack，输出 0 并退出
if ln > lh:
    print(0)
    sys.exit()

# 初始化滚动哈希所需变量
p = 29
mod = 177635683940025046467781066894531
power = [1] * (lh + 1)
for i in range(1, lh + 1):
    power[i] = (power[i - 1] * p) % mod

hash_values = [0] * (lh + 1)
for i in range(lh):
    hash_values[i + 1] = (hash_values[i] + (ord(haystack[i]) - 97 + 1) * power[i]) % mod

# 处理 haystack 的第一个子字符串
freq = [0] * 26
for i in range(ln):
    freq[ord(haystack[i]) - 97] += 1

hashes = set()
if letters == freq:
    current_hash = (hash_values[0 + ln] - hash_values[0] + mod) % mod
    current_hash = (current_hash * power[lh - 0 - ln]) % mod
    hashes.add(current_hash)

# 使用滑动窗口遍历 haystack 的剩余子字符串
for i in range(1, lh - ln + 1):
    freq[ord(haystack[i-1]) - 97] -= 1
    freq[ord(haystack[i + ln - 1]) - 97] += 1

    current_hash = (hash_values[i + ln] - hash_values[i] + mod) % mod
    current_hash = (current_hash * power[lh - i - ln]) % mod

    if letters == freq:
        hashes.add(current_hash)

print(len(hashes))  # 输出不同子字符串的数量
