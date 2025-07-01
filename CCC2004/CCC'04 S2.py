n, k = map(int, input().split())
worst = [1 for i in range(n)]
rank = [1 for i in range(n)]
score = [0 for i in range(n)]
for i in range(k):
    r = map(int, input().split())
    for y, s in enumerate(r):
        score[y] += s

    a = sorted(enumerate(score), key=lambda x: x[1])[::-1]

    cr = 0
    ls = 9999999
    for c, s in a:
        if s < ls:
            cr += 1
        rank[c] = cr
        ls = s

    for c, r in enumerate(rank):
        if r > worst[c]:
            worst[c] = r

for c, r in enumerate(rank):
    if r == 1:
        print("Yodeller {} is the TopYodeller: score {}, worst rank {}".format(c + 1, score[c], worst[c]))
