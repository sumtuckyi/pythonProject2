def binary_search_recursive(low, high, target):
    # 재귀호출을 반복하지 않을 조건
    if low > high:
        return -1

    mid = (low + high) // 2

    if target == arr[mid]:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(mid + 1, high, target)
    else:
        return binary_search_recursive(low, mid - 1, target)


N = int(input())
arr = list(map(int, input().split()))
K = int(input())
targets = list(map(int, input().split()))
arr.sort() # 오름차순으로 정렬
for i in targets:
    # 타겟을 찾으면
    if binary_search_recursive(0, len(arr) - 1, i) != -1:
        print('O', end='')
    else:
        print('X', end='')