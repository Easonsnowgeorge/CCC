total = 0
cc = 0
dd = 0
hh = 0
ss =0
a = input()
b = len(a)
c = []
d = []
h = []
s = []
z=a.index('D')
c=a[1:z]
num = len(c)
if num == 2:
    total += 1
    cc += 1
if num == 1:
    total += 2
    cc += 2
if num == 0:
    total += 3
    cc += 3
if 'A' in c:
    total += 4
    cc += 4
if 'K' in c:
    total += 3
    cc += 3
if 'Q' in c:
    total += 2
    cc += 2
if 'J' in c:
    total += 1
    cc += 1
zz=a.index('H')
d=a[z+1:zz]
num = len(d)
if num == 2:
    total += 1
    dd += 1
if num == 1:
    total += 2
    dd +=2
if num == 0:
    total += 3
    dd +=3
if 'A' in d:
    total += 4
    dd +=4
if 'K' in d:
    total += 3
    dd +=3
if 'Q' in d:
    total += 2
    dd +=2
if 'J' in d:
    total += 1
    dd +=1
zzz=a.index('S')
h=a[zz+1:zzz]
num = len(h)
if num == 2:
    total += 1
    hh += 1
if num == 1:
    total += 2
    hh +=2
if num == 0:
    total += 3
    hh +=3
if 'A' in h:
    total += 4
    hh +=4
if 'K' in h:
    total += 3
    hh +=3
if 'Q' in h:
    total += 2
    hh +=2
if 'J' in h:
    total += 1
    hh +=1
zzzz=len(a)
s=a[zzz+1:zzzz]
num = len(s)
if num == 2:
    total += 1
    ss += 1
if num == 1:
    total += 2
    ss +=2
if num == 0:
    total += 3
    ss +=3
if 'A' in s:
    total += 4
    ss +=4
if 'K' in s:
    total += 3
    ss +=3
if 'Q' in s:
    total += 2
    ss +=2
if 'J' in s:
    total += 1
    ss +=1
print("Cards Dealt                    Points")
print("Clubs", end=' ')
for i in range(len(c)):
    print(c[i], end = ' ')
print(' '*(28 - len(c)*2),end = '')
print(cc)
print("Diamonds", end=' ')
for i in range(len(d)):
    print(d[i], end = ' ')
print(' '*(25 - len(d)*2),end = '')
print(dd)
print("Hearts", end=' ')
for i in range(len(h)):
    print(h[i], end = ' ')
print(' '*(27 - len(h)*2),end = '')
print(hh)
print("Spades", end=' ')
for i in range(len(s)):
    print(s[i], end = ' ')
print(' '*(27 - len(s)*2),end = '')
print(ss)
print(' '*27, end = '')
print("Total %s"%(total))