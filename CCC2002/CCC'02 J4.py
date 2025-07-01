import math
n = int(input())
d = int(input())
if n > d:
    intval = int(n/d)
    n -= d*intval
    if n == 0:
        print(intval)
    elif n != 0:
        ans = math.gcd(n, d)
        # print(ans)
        n = int(n/ans)
        d = int(d/ans)
        print(intval, n, end = '')
        print('/', end = '')
        print(d)
else:
    ans = math.gcd(n, d)
    # print(ans)
    n = int(n / ans)
    d = int(d / ans)
    print(n, end='')
    print('/', end='')
    print(d)