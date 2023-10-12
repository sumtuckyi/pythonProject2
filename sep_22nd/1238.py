'''
bfs로 기준점으로부터 동일한 깊이의 노드를 동시에 방문,
갈 수 있는 모든 노드를 방문하면 탐색이 종료
연락을 받은 시점 = 탐색의 깊이
탐색이 종료되었을 때 가장 깊은 탐색에서 방문된 노드 중 가장 큰 값을 출력한다.
큐에 다음 탐색 노드를 추가할 때마다 최댓값을 갱신한다.
연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하이다.
노드 번호의 범위가 주어지되, 존재하지 않는 번호도 있다. -> 인접리스트를 사용
'''
from collections import deque

T = 10


def bfs(v):
    global max_v, max_depth
    q = deque([v])
    visited[v] = 1
    while q:
        now = q.popleft()
        for node in list(adj_li[now]):
            if visited[node]:
                continue
            visited[node] = visited[now] + 1

            if max_depth < visited[node] or (max_depth == visited[node] and max_v < node):
                max_depth = visited[node]
                max_v = node

            q.append(node)


for tc in range(1, 10+1):
    n, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    adj_li = [[] for _ in range(101)]
    visited = [0]*101
    max_v = -1
    max_depth = 0
    for i in range(0, n, 2):
        f = input_graph[i]
        t = input_graph[i+1]
        adj_li[f].append(t)

    bfs(start)
    print(max_v)