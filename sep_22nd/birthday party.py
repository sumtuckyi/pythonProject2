import heapq

T = int(input())


# 출발점과 도착점이 주어지면 최단 경로를 구하도록
def dijkstra(start, li, dist):
    pq = []
    heapq.heappush(pq, (start, 0))
    dist[start] = 0

    while pq:
        now, d = heapq.heappop(pq)

        if dist[now] < d:
            continue

        for item in li[now]:
            next_node = item[0]
            cost = item[1]

            new_cost = cost + d

            if dist[next_node] <= new_cost:
                continue

            dist[next_node] = new_cost
            heapq.heappush(pq, (next_node, new_cost))


for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    adj_li = [[] for _ in range(N+1)]
    adj_li_re = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        adj_li[s].append([e, w])
        adj_li_re[e].append([s, w])
    distance = [float('inf') for _ in range(N+1)]
    distance_re = [float('inf') for _ in range(N+1)]
    # x를 출발점 - 다른 나머지 노드 각각을 도착점으로
    # 다른 나머지 노드 각각을 출발점으로 -X를 도착점
    dijkstra(X, adj_li, distance)
    dijkstra(X, adj_li_re, distance_re)
    res = 0
    for i in range(1, N+1):
        res = max(res, distance[i] + distance_re[i])

    print(f'#{tc} {res}')