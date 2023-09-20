# 현재 두 로봇의 위치가 주어지면 그 사이에 몇 개의 통로가 존재하는지 확인 가능
# (N-방의 개수) (로봇1의 방번호) (로봇2의 방번호)
# N-1개 통로 정보 : (방번호1) (방번호2) (거리) -> 인접정보와 거리 파악 가능

def dfs(v, e, path):  # 시작점, 도착점, 경로
    global min_v
    visited[v] = 1
    if v == e:  # 찾고자 하는 지점이면
        for j in path:
            res = sum(path) - j
            if res < min_v:
                min_v = res
        return

    for i in range(1, N+1):
        if adj_m[v][i] == 0:
            continue
        if visited[i] == 1:
            continue
        dfs(i, e, path + [adj_m[v][i]])


N, A, B = map(int, input().split())  # 방의 개수, 로봇 A 노드, 로봇 B 노드
# 인접배열
adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0]*(N+1)
min_v = float('INF')
for _ in range(N-1):
    x, y, d = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = d  # x, y는 연결되어 있고 이때의 거리는 d이다.

# 예외적인 경우: 같은 방에 있거나 같은 통로의 끝에 있는 경우 -> 이동할 필요 없음
if A == B or adj_m[A][B] == 1:
    min_v = 0
# 로봇 사이 경로로 가능한 경우의 수 모두 구하기
dfs(A, B, [])
# 각 경로별로 이동거리의 최솟값 구하기 + 경로별로 구한 최솟값 중 최솟값 구하기
print(min_v)