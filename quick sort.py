def quick(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 두 포인터가 교차하면
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # pivot기준 왼쪽 집합을 퀵정렬
    quick(arr, start, right - 1)
    # pivot기준 오른쪽 집합을 퀵정렬
    quick(arr, right + 1, end)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')