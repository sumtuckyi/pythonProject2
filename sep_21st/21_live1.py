'''
7 11 (정점의 개수) (간선의 개수)
0 1 32 (간선노드1) (간선노드2) (비용)
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
import heapq

def prim(start):
    heap = []
    # MST에 포함되었는지 여부
    MST = [0] * V

    heapq.heappush(heap, (0, start))  # (가중치, 정점점)
    # 가중치의 누적합 저장
    sum_weight = 0

    while heap:
        weight, v = heapq.heappop(heap)  # 가중치가 가장 낮은 정점을 꺼낸다.

        # 이미 포함된 정점이라면 패스
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1
        sum_weight += weight
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 패스
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))
    return sum_weight


V, E = map(int, input().split())
# 인접행렬
graph = [[0]* V for _ in range(V)]
for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = graph[t][f] = w  # 무방향 그래프

res = prim(0)
print(f'최소비용 = {res}')
# 인접리스트
