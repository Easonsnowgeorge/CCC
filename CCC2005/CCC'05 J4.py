house_w = int(input())
house_h = int(input())
cut_w = int(input())
cut_h = int(input())
n = int(input())

grid = [[True for i in range(house_w)] for j in range(house_h)]  # 0 means white
for i in range(house_h):
    for j in range(house_w):
        if i < cut_h and j < cut_w:  # top left corner
            grid[i][j] = False  # black
        if i < cut_h and j >= house_w - cut_w:  # top rright corner
            grid[i][j] = False
        if i >= house_h - cut_h and j < cut_w:  # bottom left corner
            grid[i][j] = False
        if i >= house_h - cut_h and j >= house_w - cut_w:  # bottom right corner
            grid[i][j] = False

r = 0
c = cut_w
d = 0

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 directions
grid[r][c] = False


def next_dir(r, c, d):
    # try left
    for i in range(3):
        d_new = (d + i + 3) % 4
        r_new = r + dirs[d_new][0]
        c_new = c + dirs[d_new][1]
        if r_new >= 0 and r_new < house_h and c_new >= 0 and c_new < house_w and grid[r_new][c_new]:
            return d_new
    else:
        return -1


for i in range(n):
    d = next_dir(r, c, d)
    if d >= 0:  # continue
        r = r + dirs[d][0]
        c = c + dirs[d][1]
        grid[r][c] = False
    else:
        break

print(c + 1)
print(r + 1)