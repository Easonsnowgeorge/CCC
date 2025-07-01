import math

N = int(input())

direct = []


# add points which border the filter intervals, i.e. coeff*3^something part,
# for 12, should add (0, 4, 8, 12)
# for 27, should add (0, 1,2   3,6, 7,8   9,18,  19,20, 21,24,  25,26   27)
def add_direct_pow3(offset, n):
    if n % 3 == 0:
        third = n // 3
        add_direct_pow3(offset, third)
        add_direct_pow3(offset + 2 * third, third)
    else:
        direct.append(offset + 0)
        direct.append(offset + n)


add_direct_pow3(0, N)


# then add the rest

# find if there is a solution for f: x -> (x * 3 % N),
#   and f(f(x))=x, and neither point covered by filter, and x>0 and x<N
#   i.e. 9x % N = x, 8x % N = 0,
# try x=N/2(no, hits middle),
# (N/4, 3N/4),
# (N/8, 3N/8), (5N/8, 7N/8) ???

# then (27-1)x % N = 0, (81-x)x % N = 0, etc. (3^k - 1)x % N = 0 until k=18?
#    (k=1 would give  x*2 % N = 0, i.e. direct 1/3 and 2/3)


# check that loop: x -> x*3 % N -> (x*3 % N) *3 %N ... -> x
# does not hit the middle interval
# return True if loop is good
def check_loop(x):
    start = x

    while True:
        if (x > N / 3) and (x < 2 * N / 3):
            return False
        x = x * 3 % N
        if x == start:
            break

    return True


seeds_tested = set()
good_seeds = set()

for k in range(2, 50):  # normally N limit around 3**18??
    seed_base = 3 ** k - 1
    # print(k, seed_base)

    gcd = math.gcd(N, seed_base)  # greatest common divisor
    # print(gcd)

    if gcd > 2:
        for kk in range(1, gcd):
            seed = N // gcd * kk
            if not seed in seeds_tested:
                # print(seed, '->', check_loop(seed))
                if check_loop(seed):
                    good_seeds.add(seed)
                seeds_tested.add(seed)

# print(good_seeds)

group2 = []
group2_set = set()


# try N/4 and 3N/4, and also what leads to it
def try_seed(seed):
    if ((seed > 0 and seed < N / 3) or (seed > 2 * N / 3 and seed < N)) and not (seed in group2_set):
        group2.append(seed)
        group2_set.add(seed)

        if seed % 3 == 0:
            try_seed(seed // 3)
        if (seed + N) % 3 == 0:
            try_seed((seed + N) // 3)
        if (seed + 2 * N) % 3 == 0:
            try_seed((seed + 2 * N) // 3)


# if N % 4 == 0:
#    try_seed(N//4)
#    try_seed(3*N//4)
for seed in good_seeds:
    try_seed(seed)

result = direct + group2
result.sort()

# print(result)

for x in result:
    print(x)