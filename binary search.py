arr = [2, 4, 7, 9, 11, 19, 23]

arr.sort()


# 반복문으로 구현
def binary_search(target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    # 해당 데이터는 없습니다.
    return -1


# 재귀로 구현
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


