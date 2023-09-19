# 체스판의 크기와 말의 개수가 같기 때문에 하나의 행과 하나의 열에는 하나의 말만 올 수 있다.
# level을 행이라고 하면 i는 열이된다.
def backtracking(level):
    global cnt
    if level == N:
        cnt += 1
        return

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(level+1)
            visited[i] = 0


N = int(input())
visited = [0]*(N + 1)
cnt = 0
backtracking(0)
print(cnt)

'''
# 백트래킹으로 풀기
N = int(input())
DAT = [0] * 10
cnt = 0
def func(row):
    global cnt
    # N - 1번행까지 모두 castle을 각 행에 두었다면
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if DAT[col] == 1:   # 이미 이 열에 castle을 둔 적이 있다면
            continue        # 가지치기
        DAT[col] = 1
        func(row + 1)       # 현재를 기반으로 다음 행의 배치를 탐색
        DAT[col] = 0        # 백트래킹: 현재 열의 castle을 둔 것을 해제

func(0)
print(cnt)
'''