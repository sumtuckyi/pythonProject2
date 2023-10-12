# 최소신장트리
import heapq

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []

    for _ in range(E):
        s, d, w = map(int, input().split())
        heapq.heappush(edge, (w, s, d))

    parents = [i for i in range(V+1)]


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
        elif x < y:
            parents[y] = x
        else:
            parents[x] = y

    # 간선을 추가할 때마다 카운트, cnt가 V-1이 되면 반복 중단
    cnt = 0
    sum_weight = 0

    while True:
        w, s, d = heapq.heappop(edge)
        if find_set(s) != find_set(d):
            cnt += 1
            sum_weight += w
            union(s, d)
            if cnt == V:
                break
    # while cnt < V:
    #     w, s, d = heapq.heappop(edge)
    #     print(s, d)
    #     if find_set(s) != find_set(d):
    #         cnt += 1
    #         sum_weight += w
    #         union(s, d)

    print(f'#{tc} {sum_weight}')