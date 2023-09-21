def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return False
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y
    return True


N = int(input())
adj_m = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    adj_m[i] = row

parents = [i for i in range(N)]
print(adj_m)
for i in range(1, N):
    for j in range(i):
        if adj_m[i][j]:
            if not union(i, j):
                print('WARNING')
                exit()
print('STABLE')

# 0행은 x, 1행은 0열까지, 2행은 1열까지,