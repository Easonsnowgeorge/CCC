seat = input()
l = len(seat)
a = seat.count('A')
b = seat.count('B') + a
c = seat.count('C') + b
c2 = seat.count('C')
b2 = seat.count('B') + c2
a2 = seat.count('A') + b2
seat = " " + seat * 2
pa = [0 for i in range(2 * l + 1)]
pb = [0 for i in range(2 * l + 1)]
pc = [0 for i in range(2 * l + 1)]

for i in range(1, 2 * l + 1):
    pa[i] = pa[i - 1] + (seat[i] == 'A')
    pb[i] = pb[i - 1] + (seat[i] == 'B')
    pc[i] = pc[i - 1] + (seat[i] == 'C')

mm = 1 << 32

for i in range(l + 1):
    mm = min(mm, pc[i + b] - pc[i] + max(pb[i + a] - pb[i], pa[i + b] - pa[i + a]))
    mm = min(mm, pa[i + b2] - pa[i] + max(pb[i + c2] - pb[i], pc[i + b2] - pc[i + c2]))

print(mm)