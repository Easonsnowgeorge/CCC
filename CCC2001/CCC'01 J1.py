n=int(input())
a=1
x=[]
while a<=n:
    b=n-a
    str=a*"*"+2*b*" "+a*"*"
    x.append(str)
    a+=2
    print(str)


x.reverse()
for i in range(1,int(n/2)+1):
    print(x[i])