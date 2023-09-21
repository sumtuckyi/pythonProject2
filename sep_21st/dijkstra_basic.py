# N은 노드의 마지막 번호로 노드의 개수는 N+1개
# 모든 연결 지점을 거쳐야 하는 것은 아님/ 출발지(0) -도착지(N)만 고려하면 됨
# dfs, 재귀
import heapq

T = int(input())


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        d, now = heapq.heappop(pq)

        if distance[now] < d:
            continue

        for i in range(N+1):  # node의 형식은 [node_n, w]
            if not adj_m[now][i]:
                continue
            can_node = i
            cost = adj_m[now][i]

            n_cost = d + cost
            if n_cost >= distance[can_node]:
                continue
            distance[can_node] = n_cost
            heapq.heappush(pq, (n_cost, can_node))


for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
    distance = [float('inf') for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        adj_m[s][e] = w
    dijkstra(0)

    print(f'#{tc} {distance[N]}')