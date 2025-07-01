w=0
l=0
for i in range(6):
    wl = input()
    if wl == "W":
        w += 1
    elif wl == "L":
        l += 1
if w == 5 or w == 6:
    print(1)
elif w == 3 or w == 4:
    print(2)
elif w == 1 or w == 2:
    print(3)
else:
    print(-1)