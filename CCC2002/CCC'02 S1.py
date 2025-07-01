a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
total = 0
l=[]
for w in range(int(e/a)+1):
    for x in range(int(e/b)+1):
        for y in range(int(e/c)+1):
            for z in range(int(e/d)+1):
                if w==x==y==z==0:
                    continue
                if a * w+b*x+c*y+d*z==e:
                    print("# of PINK is %s # of GREEN is %s # of RED is %s # of ORANGE is %s"%(w,x,y,z))
                    total += 1
                    g=w+y+z+x
                    l.append(g)
print("Total combinations is %s." %(total))
# print(l)
print("Minimum number of tickets to print is "+str(min(l))+".")