R = int(input())
L = int(input())
rows = [int(input().replace(" ", ""), 2) for _ in range(R)]  # convert to int to use built in XOR

possible = [set() for _ in range(R)]
possible[0] = {rows[0]}  # base case

for i in range(1, R):
    possible[i].add(rows[i])  # option 1: don't press button
    for prev in possible[i - 1]:
        possible[i].add(rows[i] ^ prev)  # option 2: xor with previous row

print(len(possible[-1]))