# 해당 칸의 충전지 용량으로 갈 수 있는 범위의 정류장이 다음선택지가 됨
# 항상 1번에서 출발하여 N번에 도착

def backtracking(i, N, cnt):
    global min_v
    if cnt > min_v:
        return
    # 종착점에 도착하면
    if i == N:
        if cnt < min_v:
            min_v = cnt
        return
    k = row[i]  # i정류장에서의 충전지 용량
    for j in range(k, 0, -1):
        if i+j <= N:
            backtracking(i + j, N, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    row = list(map(int, input().split()))
    N = row[0]  # 정류장의 수
    min_v = float('inf')
    backtracking(1, N, 0)
    print(f'#{tc} {min_v-1}')


# 다른 풀이
# def dfs(idx, sumv):
#     global answer
#     if answer < sumv: return
#     if idx >= N:
#         answer = sumv
#         return
#     count = station[idx]
#     for i in range(count, 0, -1):
#         dfs(idx + i, sumv + 1)
#
# T = int(input())
# for tc in range(1, T + 1):
#     answer = float('INF')
#     station = list(map(int,input().split()))
#     N = station.pop(0) - 1
#     dfs(0, -1)
