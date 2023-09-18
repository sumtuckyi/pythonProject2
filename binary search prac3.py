# 찾는 수가 arr에 들어있을 때, 이 수를 찾기 위해 이진탐색을 수행할 경우
# 왼쪽 구간과 오른쪽 구간을 모두 탐색하여 찾게되는 경우를 카운트하여 출력
# 단, mid=target으로 찾게되는 경우도 포함한다.

def binary_search_recursive(low, high, target):
    global l, r, pre
    # 재귀호출을 반복하지 않을 조건
    # target값이 존재하지 않는 경우
    if low > high:
        return -1

    mid = (low + high) // 2

    if target == arr[mid]:
        return mid

    elif arr[mid] < target:
        if pre == 'r':
            return -1
        pre = 'r'
        return binary_search_recursive(mid + 1, high, target)
    else:
        if pre == 'l':
            return -1
        pre = 'l'
        return binary_search_recursive(low, mid - 1, target)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    m = list(map(int, input().split()))
    cnt = 0
    # 바로 이전의 탐색구간이 오른쪽인지 왼쪽인지
    for i in m:
        pre = ''
        # 타겟을 찾은 경우
        if binary_search_recursive(0, N-1, i) != -1:
            cnt += 1
    print(f'#{tc} {cnt}')
