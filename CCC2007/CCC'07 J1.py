a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
   if b > c:
       print(b)
   if c>b:
       print(c)
if b > a and b > c:
   if c>a:
       print(c)
   if a>c:
       print(a)
if c >a and c > b:
   if a >b:
       print(a)
   if b>a:
       print(b)