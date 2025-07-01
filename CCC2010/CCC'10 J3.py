d = 0
e = 0
for i in range(100):
    a = input()
    z = a.split()
    if a == '7':
        break

    if a[0] == '1'and z[1] == 'A':
        d = z[2]
    if z[0] == '2' and z[1] == 'A':
        print(d)

    if a[0] == '1'and z[1] == 'B':
        e = z[2]
    if z[0] == '2' and z[1] == 'B':
        print(e)

    if a[0] == '3':
        d =int(d) + int(e)

    if a[0] == '4'and z[1] == 'A' and z[2] == 'B':
        d = int(d) * int(e)
    if a[0] == '4'and z[1] == 'B' and z[2] == 'A':
        e = int(d) * int(e)

    if a[0] == '5'and z[1] == 'A' and z[2] == 'B':
        d = int(d)-int(e)
    if a[0] == '5' and z[1] == 'A' and z[2] == 'A':
        d = int(d)-int(d)
    if a[0] == '5' and z[1] == 'B' and z[2] == 'B':
        d = 0

    if a[0] == '6'and z[1] == 'A' and z[2] == 'B':
        d = int(d)/int(e)
    if a[0] == '6'and z[1] == 'B' and z[2] == 'A':
        e = int(int(e)/int(d))
