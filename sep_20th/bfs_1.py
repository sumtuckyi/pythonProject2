# 코스타그램
# append(), popleft()
from collections import deque

def bfs(v):
    cnt = 0
    visited[v] = 1
    queue = deque([v])
    while queue:
        now = queue.popleft()
        for i in range(1, N+1):
            if visited[i]:
                continue
            if adj_m[now][i]:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


N = int(input())
M = int(input())
adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited =[0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adj_m[a][b] = adj_m[b][a] = 1
coco = int(input())
print(bfs(coco))
