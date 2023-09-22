# 2 ≤ M,N ≤ 1,000
# 상자의 가로, 세로 길이
# 처음부터 모든토마토가 익어있다면(모두 1이라면) 0을, 모두 익지 못하는 조건이면 -1을, 모두 익을 수 있다면 최소 날짜를 출력
# 입력을 받을 때 확인하지 않고 bfs탐색을 통해 0을 출력할지 검토,
M, N = map(int, input().split())
box = [[] for _ in range(N)]
for i in range(N):
     box[i].extend(list(map(int, input().split())))
