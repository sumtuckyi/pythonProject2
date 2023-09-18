# 정렬이 끝난 리스트의 N//2번째 원소를 출력, 병합단계에서 왼쪽 마지막 원소가 오른쪽 집합의 마지막 원소보다 큰 경우를 카운트하여 출력
# L[0:N//2], L[N//2:N]으로 분할
from collections import deque
import itertools
T = int(input())


def merge(a, b):
    global cnt
    temp = []  # 두 부분집합을 병합한 결과
    tof = True
    l = 0
    r = 0
    while len(a) > l or len(b) > r:  # 두 부분집합 중 하나라도 원소가 남아있다면
        if len(a) > l and len(b) > r:  # 두 부분집합 모두 원소가 남아있다면
            if tof:
                if a[-1] > b[-1]:
                    cnt += 1
                    tof = False
            if a[l] <= b[r]:  # 같은 값이라면 왼쪽의 값을 먼저
                temp.append(a[l])
                l += 1
            else:
                temp.append(b[r])
                r += 1
        elif len(a) > l:  # 왼쪽에만 원소가 남았을 때
            temp.append(a[l])
            l += 1
        elif len(b) > r:  # 오른쪽에만 원소가 남았을 때
            temp.append(b[r])
            r += 1
    return temp


def merge_sort(li, N):
    # 부분집합의 크기가 1이면 부분집합을 그대로 반환
    if N == 1:
        return li

    left = li[:N//2]
    right = li[N//2:N]

    left = merge_sort(left, len(left))
    right = merge_sort(right, len(right))

    return merge(left, right)


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr, N)
    print(f'#{tc} {result[N//2]} {cnt}')