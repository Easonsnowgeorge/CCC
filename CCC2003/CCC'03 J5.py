floor = []
rooms = []
t = int(input())
r = int(input())
c = int(input())
for i in range(r):
    a = list(map(str, input()))
    floor.append(a)
res=[]
ans = []
def dfs(x,y):
    floor[x][y] = 'I'
    rooms.append((x,y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x2 = x+dx[i]
        y2 = y+dy[i]
        if x2 >= 0 and y2 >= 0 and x2 < r and y2 < c and floor[x2][y2] == ".":
            dfs(x2, y2)
for x in range(r):
    for y in range(c):
        if floor[x][y]==".":
            dfs(x,y)
            res.append(len(rooms))
ha = 0
ans.append(res[0])
for i in range(len(res)-1):
    ans.append(res[i+1]-res[i])
ans.sort()
while t >= 0:
    if len(ans) == 0:
        break
    if t - ans[-1] < 0:
        break
    hehaw = int(ans[-1])
    t-=hehaw
    ans.remove(hehaw)
    ha += 1
if ha == 1:
    print("%s room, %s square metre(s) left over" % (ha, t))
else:
    print("%s rooms, %s square metre(s) left over" % (ha, t))