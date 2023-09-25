T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = list(input())  # 암호화된 16진수는 리스트로
    key = int(input(), 16)  # 키는 정수로 변환

    H = [0] * N
    for i in range(N):
        H[i] = int(P[i], 16) ^ key  # 리스트에는 복호화된 각 자릿수가 저장됨
    print(f'#{tc}', end='')
    for x in H:
        print(f'{x:X}', end='')


# 2문
def backtracking(level, N, total):
    global max_v
    if level == N:
        if max_v < total:
            max_v = total
    # 순열 구현
    # 반복문
    for j in range(i, N):
        p[i], p[j] = p[j], p[i]
        backtracking(level+1, N, total + arr[level][p[i]])
        p[i], p[j] = p[j], p[i]


p = [i for i in range(N)]  # N개의 열(visited역할)
arr = [list(map(int, input().split())) for _ in range(N)]
