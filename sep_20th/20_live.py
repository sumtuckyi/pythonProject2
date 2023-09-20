# 그래프

# 인접행렬
'''
(+)구현이 쉽다.
(-)메모리 낭비 - 연결되지 않은 관계(0)도 저장한다.
'''
arr_f = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# 인접리스트
'''
(+)갈 수 있는 지점만 저장한다.
각 노드마다 갈 수 있는 지점의 개수가 다르기 때문에 range()를 사용할 때 index 주의
'''
arr_s = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]

N = len(arr_f)
# 그래프 탐색
# 1. DFS
#   -stack : 같은 층위라면 큰 번호의 노드가 더 늦게 스택에 쌓이므로 먼저 출력됨
def dfs_stack(v):
    visited = []
    stack = [v]
    while stack:
        now = stack.pop()  # 탐색 기준 노드
        if now in visited: # 이미 방문한 노드라면
            continue

        visited.append(now)
        # for next in range(N):
        for next in range(N-1, -1, -1):
            # pass 조건
            if arr_f[now][next] == 0:
                continue
            stack.append(next)
    return visited


print('dfs stack:', end=' ')
print(*dfs_stack(0))

#   -재귀
# visited = [0]*N
# def dfs_recursive(start):
#     visited[start] = 1
#     print(start, end=' ')
#
#     for next in range(N):
#         if arr_f[start][next] == 0:
#             continue
#
#         if visited[next]:
#             continue
#
#         dfs_recursive(next)
#
#
# print('dfs recursive:', end=' ')
# dfs_recursive(0)


# 2. BFS
visited = [0]*N
def bfs(start):
    queue = [start]
    visited[start] = 1
    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for next in range(N):
            if arr_f[now][next] == 0:
                continue

            if visited[next]:
                continue

            visited[next] = 1
            queue.append(next)

print()
print('bfs:', end=' ')
bfs(0)

