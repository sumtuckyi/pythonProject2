# 주어진 일이 모두 성공할 확률 중 최댓값을 구하라
T = int(input())


def dfs(level, total):
    global max_v
    if total <= max_v:
        return
    if level == N+1:
        if total > max_v:
            max_v = total
        return

    for i in range(1, N+1):  # N개의 일을 탐색
        if visited[i] == 1:  # 이미 처리된 일이면
            continue
        if adj_m[level][i-1] == 0:
            continue
        visited[i] = 1
        dfs(level+1, total*adj_m[level][i-1]/100)
        visited[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    visited = [0]*(N+1)
    max_v = 0
    adj_m = [[]] + [list(map(int, input().split())) for _ in range(N)]
    dfs(1, 1)
    max_v = round(max_v * 100, 6)
    print(f'#{tc} {max_v:.6f}')