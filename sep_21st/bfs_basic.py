# 출발점은 항상 [0][0]이고 도착점은 항상 [N-1][N-1]
#
# from collections import deque
#
#
# def bfs(x, y, total):
#     global min_v
#     if x == N - 1 and y == N - 1:
#         if total < min_v:
#             min_v = total
#         return
#     q.append((x, y))
#     visited[x][y] = 1
#     while q:
#         now_x, now_y = q.popleft()
#         for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             if 0 <= now_x + i < N and 0 <= now_y + j < N:
#                 if visited[now_x + i][now_y + j]:
#                     continue
#                 if total > min_v:
#                     continue
#                 visited[now_x + i][now_y + j] = 1
#                 temp = abs(arr[now_x][now_y] - arr[now_x + i][now_y + j])
#                 total += (1 + temp)
#                 bfs(now_x + i, now_y + j, total)
#                 visited[now_x + i][now_y + j] = 0
#                 total -= (1 + temp)
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     min_v = float('inf')
#     q = deque()
#     bfs(0, 0, 0)
#     print(f'#{tc} {min_v}')

import heapq

T = int(input())


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
            if 0 <= x + i < N and 0 <= y + j < N:
                can = (x + i, y + j)
                temp = arr[x + i][y + j] - arr[x][y] if arr[x + i][y + j] > arr[x][y] else 0
                cost = temp + 1

                n_cost = d + cost
                if n_cost >= distance[can[0]][can[1]]:
                    continue
                distance[can[0]][can[1]] = n_cost
                heapq.heappush(pq, (n_cost, can))


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    dijkstra((0, 0))
    print(f'#{tc} {distance[N-1][N-1]}')

