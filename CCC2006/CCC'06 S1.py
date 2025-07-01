m = input()
f = input()
n = int(input())
a = []
b = []
for i in range(10):
    if ord(m[i]) <= 90:
        a.append(True)
    else:
        a.append(False)
for i in range(10):
    if ord(f[i]) <= 90:
        b.append(True)
    else:
        b.append(False)

for i in range(n):
    baby = input()
    c = 0
    for j in range(len(baby)):
        if ord(baby[j]) <= 90:
            if a[2*j] == 1 or b[2*j] == 1:
                continue
            else:
                print("Not their baby!")
                c = 1
                break
        else:
            if a[2*j+1] == 1 or b[2*j+1] == 1:
                print("Not their baby!")
                c = 1
                break
            else:
                continue
    if c != 1:
        print("Possible baby.")