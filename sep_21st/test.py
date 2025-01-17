from collections import defaultdict


def find(n):
    if par[n] == n:
        return n
    else:
        par[n] = find(par[n])
    return par[n]


def union(a, b):
    if find(a) != find(b):
        if rank[find(a)] > rank[find(b)]:
            par[find(b)] = find(a)
        else:
            par[find(a)] = find(b)
            if rank[find(a)] == rank[find(b)]:
                rank[find(b)] += 1
    else:
        return


N = int(input())
par = {chr(i): chr(i) for i in range(65, 90 + 1)}
rank = {chr(i) : i for i in range(65, 90 + 1)}
for _ in range(N):
    n1, n2 = input().split()
    union(n1, n2)

cnt = 0
g = 0
new = defaultdict(int)
for value in par.values():
    new[find(value)] += 1
for value in new.values():
    if value > 1:
        cnt += 1
for key, value in par.items():
    if key == value:
        g += 1
print(cnt)  # 집단의 수
print(g - cnt)  # 개인연주자의 수
