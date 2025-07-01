n = int(input())
for i in range(n):
    y, m, d = list(map(int, input().split()))
    if y < 1989:
        print("Yes")
    elif y == 1989:
        if m > 2:
            print("No")
        elif m < 2:
            print("Yes")
        else:
            if d <= 27:
                print("Yes")
            else:
                print("No")
    else:
        print("No")