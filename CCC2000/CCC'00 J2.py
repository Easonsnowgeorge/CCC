l = int(input())
h = int(input())
cnt = 0
for i in range(l, h+1):
    a = str(i)
    f = 1
    for j in range(len(a)//2 + 1):
        if (a[j] == "1" or a[j] == "0" or a[j] == "8") and a[len(a)-(j+1)] == a[j]:
            continue
        elif a[j] == "6" and a[len(a)-(j+1)] == "9":
            continue
        elif a[j] == "9" and a[len(a)-(j+1)] == "6":
            continue
        else:
            f = 0
            break
    if f == 1:
        cnt += 1
print(cnt)