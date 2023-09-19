def backtracking(level, total):
    global min_c
    if total > min_c:
        return
    if level == N:
        if total < min_c:
            min_c = total

    for i in range(N):
        if checked[i] == 0:
            checked[i] = 1
            backtracking(level + 1, total+costs[level][i])
            checked[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    checked = [0]*(N+1)
    min_c = float('inf')
    backtracking(0, 0)
    print(f'#{tc} {min_c}')