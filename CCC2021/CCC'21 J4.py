from collections import Counter

# 读取书籍的排列
books = input()
# 统计每种书的数量
count = Counter(books)

# 初始化错位书籍的计数器
ls = sl = ml = lm = sm = ms = 0

# 统计'L'区域中的'S'和'M'
for i in range(count["L"]):
    if books[i] == "S":
        sl += 1
    elif books[i] == "M":
        ml += 1

# 统计'M'区域中的'S'和'L'
for i in range(count["M"]):
    i += count["L"]
    if books[i] == "S":
        sm += 1
    elif books[i] == "L":
        lm += 1

# 统计'S'区域中的'L'和'M'
for i in range(count["L"] + count["M"], len(books)):
    if books[i] == "L":
        ls += 1
    elif books[i] == "M":
        ms += 1

# 初始化交换次数
swaps = 0

# 交换'S'和'L'
ls_swap = min(sl, ls)
swaps += ls_swap
sl, ls = sl - ls_swap, ls - ls_swap

# 交换'S'和'M'
sm_swap = min(sm, ms)
swaps += sm_swap
sm, ms = sm - sm_swap, ms - sm_swap

# 交换'M'和'L'
ml_swap = min(ml, lm)
swaps += ml_swap
ml, lm = ml - ml_swap, lm - ml_swap

# 处理剩余的错位，这些交换需要两步
slm = min(sl, lm, ms)
swaps += slm * 2
sl -= slm
lm -= slm
ms -= slm

sml = min(ls, ml, sm)
swaps += 2 * sml
ls -= slm
ml -= slm
sm -= slm

# 打印总的交换次数
print(swaps)
