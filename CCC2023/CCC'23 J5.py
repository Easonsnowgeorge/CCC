# 读取要查找的单词
word = input()

# 读取网格的行数和列数
ROWS = int(input())
COLS = int(input())

# 初始化网格并读取每行的数据
grid = []
for i in range(ROWS):
    grid.append(input().split())

# 初始化找到的单词数量为0
count = 0

# 定义8个可能的方向（上、上右、右、下右、下、下左、左、上左）
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 定义一个函数来检查特定方向上的单词
def check(row, col, dr, dc, index, turned):
    global count
    # 检查当前位置是否有效且是否匹配单词的当前字母
    if ROWS > row >= 0 and COLS > col >= 0 and grid[row][col] == word[index]:
        # 如果找到了整个单词，增加计数
        if index == len(word) - 1:
            count += 1
            return

        # 继续在当前方向上检查下一个字母
        check(row + dr, col + dc, dr, dc, index + 1, turned)

        # 如果还没有转弯，尝试在垂直方向上转弯并检查
        if not turned:
            check(row - dc, col + dr, -dc, dr, index + 1, True)
            check(row + dc, col - dr, dc, -dr, index + 1, True)

# 遍历网格的每个位置
for i in range(ROWS):
    for j in range(COLS):
        # 如果当前位置匹配单词的第一个字母，开始在所有方向上搜索
        if grid[i][j] == word[0]:
            for r, c in directions:
                check(i + r, j + c, r, c, 1, False)

# 打印找到的单词数量
print(count)
