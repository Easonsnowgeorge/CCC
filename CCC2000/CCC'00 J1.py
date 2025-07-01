x = input().split()

a = int(x[0])

b = int(x[1])

c = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
for i in range(6):
    print(c[i], end=" ")
print(c[6])
d = []
for i in range(a - 1):
    d.append("   ")
for i in range(1, 10):
    d.append("  " + str(i))
for i in range(10, b + 1):
    d.append(" " + str(i))

for i in range(int(len(d) / 7)):
    print("%s %s %s %s %s %s %s" % (
    d[i * 7], d[i * 7 + 1], d[i * 7 + 2], d[i * 7 + 3], d[i * 7 + 4], d[i * 7 + 5], d[i * 7 + 6]))
e = int(len(d) % 7)
if e != 0:

    for i in range(e - 1):
        print(d[-e], end=" ")
        e -= 1
    print(d[-1])