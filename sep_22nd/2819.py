# 격자판의 크기가 4*4이므로 완전탐색이 가능함
# -> 격자판의 각 칸에서 탐색을 시작
# 숫자가 0으로 시작할 수 있음 -> 문자열을 사용하면 편리
# 서로 다른 7자리 수들의 개수를 구하여라 -> set으로 중복을 제거
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(y, x, number):
    if len(number) == 7:
        result.add(number)
        return

    for k in range(4):
        ny = y + d[k][0]
        nx = x + d[k][1]

        if ny < 0 or ny >= 4:
            continue

        if nx < 0 or nx >= 4:
            continue

        dfs(nx, ny, number + maps[ny][nx])


T = int(input())
for tc in range(1, T + 1):
    maps = [input().split() for _ in range(4)]
    # 중복제거
    result = set()
    # 격자판의 모든 칸을 시작지점으로 삼아 반복
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')