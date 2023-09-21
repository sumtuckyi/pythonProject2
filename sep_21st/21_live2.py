'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 모든 간선들 중 비용이 가장 적은 걸 우선 고르자 -> sort()이용
# Kruskal 알고리즘
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# ★w를 기준으로 정렬★
edge.sort(key=lambda x:x[2])

# 사이클 발생여부 확인 -> union-find이용
# 두 정점을 연결하기에 앞서 이미 두 정점이 같은 집합에 속한다면 연결할 시에 사이클이 발생하게 됨
parents = [i for i in range(V)]


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


cnt = 0  # 현재 방문한 정점의 수
sum_weight = 0
for f, t, w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if cnt == V:
            break

print(f'최소비용 = {sum_weight}')