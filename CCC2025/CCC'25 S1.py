a,b,x,y = map(int,input().split())

p1 = (a+y)*2 + max(b,x)*2
p2 = (a+x)*2 + max(b,y)*2

p = min(p1,p2)

print(p)