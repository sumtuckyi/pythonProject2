'''
1486
1952
2819
1238
'''
# 1486문
'''
N의 값이 10이하인 경우에나 완전탐색을 고려해볼 수 있다.
10을 넘어가면 백트래킹으로 가지치기를 해줘야 제한된 시간 안에 문제를 해결할 수 있다.
데이터의 크기가 그보다 더 커지면
그리디, dp, union-find, 이진탐색 등 다른 알고리즘을 고려해야 시간복잡도를 줄일 수 있다. 
'''
# 가능한 모든 경우를 고려한다.(N명의 점원 중 1~N명을 뽑는 경우의 수를 모두 고려)
#  N의 범위가 10보다 크기 때문에 가지치기할 조건을 구한다.
# 조합 이용 - 집합의 해당 요소를 포함할 것인지 하지 않을 것인지 나누어서 재귀호출
#
def recur(level, acc_height):
    global ans

    # 기저 조건
    if level == N:
        return
    # 가지치기
    if acc_height >= B:
        ans = min(ans, acc_height)
        return

    # 조합 구현
    # 해당 점원을 쓰는 경우
    recur(level + 1, acc_height + heights[level])
    # 쓰지 않는 경우
    recur(level + 1, heights[level])


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = int(1e9)  # 차이의 최솟값
    recur(0, 0)
    print(f'#{tc} {ans-B}')
