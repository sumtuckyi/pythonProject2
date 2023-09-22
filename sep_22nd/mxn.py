import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))  # start는 튜플
    distance[start[0]][start[1]] = 0

    while pq:
        d, now = heapq.heappop(pq)
        x, y = now[0], now[1]

        if distance[x][y] < d:
            continue

        # 인접노드 탐색
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + i < N and 0 <= y + j < M:
                can = (x + i, y + j)
                cost = arr[x + i][y + j]

                n_cost = d + cost
                if n_cost >= distance[can[0]][can[1]]:
                    continue
                distance[can[0]][can[1]] = n_cost
                heapq.heappush(pq, (n_cost, can))


N, M = map(int, input().split())  # 행, 열
arr = [list(map(int, input().split())) for _ in range(N)]
distance = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
dijkstra((0, 0))
print(distance[N-1][M-1])