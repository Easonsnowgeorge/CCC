z = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(1000):
    a = input()
    a.split()
    b = len(a)
    if a == 'quit!':
        break
    if len(a) >= 4 and a[b-1] == 'r' and a[b-2] == 'o' and a[b-3] not in z:
        for i in range(b-1):
            print(a[b - (b-i)], end = '')
        print("u", end = '')
        print("r")
    else:
        print(a)