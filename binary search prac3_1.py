def binary_search(target):
    start, end = 0, n - 1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            if check == 1:
                break
            check = 1
            end = mid - 1
        else:
            if check == 2:
                break
            check = 2
            start = mid + 1
    return False

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binary_search(num)
    print(f'#{tc} {total}')