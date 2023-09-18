# target이 범위, 해당 범위에 속하는 광물의 수를 출력
# 범위의 최솟값을 먼저 target으로 삼아서 이진탐색,
# 범위의 최솟값보다 큰 값들이 모여있는 집합에서 범위의 최댓값을 기준으로 탐색
def binary_search_recursive1(low, high, target):
    # 재귀호출을 반복하지 않을 조건
    # 범위의 시작인덱스와 종료인덱스가 같아지는 경우
    if low >= high:
        if arr[low] < target:
            return low + 1
        else:
            return low

    mid = (low + high) // 2
    # arr에서 범위의 최솟값과 일치하는 가장 앞쪽 인덱스를 찾아라
    if target == arr[mid]:
        return binary_search_recursive1(0, mid - 1, target)
        # return mid

    elif arr[mid] < target:
        return binary_search_recursive1(mid + 1, high, target)
    else:
        return binary_search_recursive1(low, mid - 1, target)

def binary_search_recursive2(low, high, target):
    # 재귀호출을 반복하지 않을 조건
    if low >= high:
        if arr[high] > target:
            return high - 1
        else:
            return high

    mid = (low + high) // 2 # 범위가 두 칸이면 앞의 값
    # arr에서 범위의 최솟값과 일치하는 가장 앞쪽 인덱스를 찾아라
    if target == arr[mid]:
        return binary_search_recursive2(mid + 1, N-1, target)
        # return mid

    elif arr[mid] < target:
        return binary_search_recursive2(mid + 1, high, target)
    else:
        return binary_search_recursive2(low, mid - 1, target)


N, Q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
needs = []

for _ in range(Q):
    a, b = map(int, input().split())
    needs.append((a, b))
for i, j in needs:
    min_i = binary_search_recursive1(0, len(arr)-1, i)
    max_i = binary_search_recursive2(0, len(arr)-1, j)
    print(max_i-min_i+1)