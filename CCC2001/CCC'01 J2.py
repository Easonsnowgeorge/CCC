x=int(input())
m=int(input())
flag=0
for n in range(99):
    if (x*n)%m==1:
        print(n)
        flag+=1
        break
if flag==0:
    print("No such integer exists.")
