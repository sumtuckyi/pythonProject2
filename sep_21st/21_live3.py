'''
누적거리가 가장 짧은 경로를 고르자
우선순위 큐를 활용
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
import heapq

n, m = map(int, input().split())
# 인접리스트
graph = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])  # f에서 t로 갈 수 있음

# 누적 거리를 계속 저장
INF = int(1e9)
distance = [INF] * n


def dijkstra(start):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))  # 우선순위 큐에는 (누적 거리, 노드 번호) 삽입
    distance[start] = 0  # 출발점까지의 누적거리 초기화

    while pq:
        # 현시점에서 누적 거리가 가장 짧은 노드 꺼내기
        dist, now = heapq.heappop(pq)

        # distance[now]의 값으로 이미 더 짧은 누적 거리가 구해져있다면 패스
        if distance[now] < dist:
            continue

        # 큐에서 꺼낸 노드의 인접 노드를 확인
        for next in graph[now]:  # graph[now]는 now에서 갈 수 있는 [노드 번호와 가중치]가 저장된 2차원 리스트
            next_node = next[0]  # 인접 노드 번호
            cost = next[1]  # 인접 노드까지의 가중치

            # next_node로 가기 위한 누적 거리 구하기
            # dist는 now까지의 누적 거리
            new_cost = dist + cost

            # 새로 구한 누적 거리가 기존 누적 거리보다 길면 패스
            if distance[next_node] <= new_cost:
                continue
            # 새로 구한 누적 거리가 기존 누적 거리보다 짧으면 distance 배열 값을 갱신
            distance[next_node] = new_cost

            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)
