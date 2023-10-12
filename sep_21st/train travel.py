# 0번에서 출발하여 N-1번 도착
# 정점의 개수는 N개
import heapq

N, T = map(int, input().split())
graph = [[] for _ in range(N)]
adj_m = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(T):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])
    adj_m[f][t] = 1
distance = [float('inf') for _ in range(N)]
visited = [0]*N
tof = True


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        d, now = heapq.heappop(pq)

        if distance[now] < d:
            continue

        for item in graph[now]:  # node의 형식은 [node_n, w]
            can_node = item[0]
            cost = item[1]

            n_cost = d + cost
            if n_cost >= distance[can_node]:
                continue
            distance[can_node] = n_cost
            heapq.heappush(pq, (n_cost, can_node))


# 만약 연결 되어있지 않다면 impossible 출력
def dfs(v):
    visited[v] = 1
    for i in range(N):
        if not adj_m[v][i]:
            continue
        if visited[i]:
            continue
        dfs(i)


dijkstra(0)
dfs(0)
if not visited[N-1]:
    tof = False

if not tof:
    print('impossible')
else:
    print(distance[N-1])

# 다른 풀이
import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float('inf') for _ in range(n)]
visited = [False]*n
pq = []

def dijkstra():
    distance[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        # 이미 방문한 노드라면 패스???
        # if visited[cur_node]:
        #     continue
        # visited[cur_node] = True

        for next_node, edge_cost in graph[cur_node]:
            total_cost = cur_cost + edge_cost
            if distance[next_node] > total_cost:
                distance[next_node] = total_cost
                heapq.heappush(pq, (total_cost, next_node))

# 목표한 지점(n-1)과 연결되어 있지 않았다면 distance[n-1]은 여전히 초기화 값일 것임
if distance[n-1] == float('inf'):
    print('impossible')
else:
    print(distance[n-1])

for _ in range(e):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))


