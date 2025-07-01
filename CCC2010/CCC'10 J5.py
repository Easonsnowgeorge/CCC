def bfs():
  global ans
  moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2), (-2, 1), (-2, -1)]
  a = []
  a.append((sx, sy, 0))
  while (len(a) > 0):
    spot = a.pop(0)
    if spot[0] == ex and spot[1] == ey:
      ans = spot[2]
      break
    for move in moves:
      newx = spot[0] + move[0]
      newy = spot[1] + move[1]
      if 1 <= newx <= 8 and 1 <= newy <= 8:
        a.append((newx, newy, spot[2] + 1))
ans = 0
sx, sy = list(map(int, input().split(" ")))
ex, ey = list(map(int, input().split(" ")))
bfs()
print(ans)