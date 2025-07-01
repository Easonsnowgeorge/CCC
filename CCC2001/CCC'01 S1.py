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


#ccc waterloo 2001 s1 question:)
#process all the info check
#sort the info into lists check
#run a bunch of ifs check
#calculate the points check
#print with good spacing
#test and win:)
Info = input()
sort_num = -1
Types = ["C","D","H","S"]
Clubs = []
Diamonds = []
Hearts = []
Spades = []
all_types = [Clubs,Diamonds,Hearts,Spades]
Clubs_points = 0
Diamonds_points = 0
Hearts_points = 0
Spades_points = 0
all_points = [Clubs_points,Diamonds_points,Hearts_points,Spades_points]
Final_points = Clubs_points + Diamonds_points + Hearts_points + Spades_points
for i in range(len(Info)):
    if Info[i] in Types:
        sort_num += 1
    else:
        all_types[sort_num].append(Info[i])
for i in range(4):
    if "A" in all_types[i]:
        all_points[i] += 4
    if "K" in all_types[i]:
        all_points[i] += 3
    if "Q" in all_types[i]:
        all_points[i] += 2
    if "J" in all_types[i]:
        all_points[i] += 1
    if len(all_types[i]) == 0:
        all_points[i] += 3
    if len(all_types[i]) == 1:
        all_points[i] += 2
    if len(all_types[i]) == 2:
        all_points[i] += 1
print("Cards Dealt                       Points")
length = 31
#26
Clubber = ""
Diamands = ""
Harts = ""
Spaides = ""
lines = [Clubber,Diamands,Harts,Spaides]
all_names = ["Clubs","Diamonds","Hearts","Spades"]
#to check the main data so it's easier debugging
################   /
#print(all_types) #<--------------
#print(all_points) #<--------------
################   \
#to check the main data so it's easier debugging
for i in range(4):
    lines[i] += all_names[i]

    for j in range(31-len(all_names[i])):
        if len(all_types[i]) - j > 0:
            lines[i] += " "
            lines[i] += all_types[i][j]
        else:
            for l in range((37 - len(lines[i]))-int(all_points[i]/10)):
                lines[i] += " "
    lines[i] += str(all_points[i])
for i in range(4):
    print(lines[i])
Final_points = all_points[0] + all_points[1] + all_points[2] + all_points[3]
if Final_points < 10:
    print("                              Total ",Final_points)
else:
    print("                              Total",Final_points)