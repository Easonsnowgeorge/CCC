x = []
y = []
while (True):
    a, b = input().split()
    x.append(a)
    y.append(int(b))
    if a == "Waterloo":
        break
c = min(y)
d = y.index(c)
print(x[d])