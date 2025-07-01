a = int(input())
b = int(input())
c = int(input())
d = int(input())
total = 0
for x in range(101):
    for y in range(101):
        for z in range(101):
            if x==y==z==0:
                continue
            if a * x+b*y+c*z<=d:
                print("%s Brown Trout, %s Northern Pike, %s Yellow Pickerel"%(x,y,z))
                total += 1
print("Number of ways to catch fish: %s" %(total))