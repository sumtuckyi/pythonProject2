# 정수 n을 1, 2, 3의 합으로 나타낼 수 있는 경우의 수(중복 사용 가능, 순서가 다른 경우도 다른 경우로 봄)
n = int(input())
arr = [1, 2, 3]
cnt = 0


def backtracking(total):
    global cnt
    if total > n:
        return

    if total == n:
        cnt += 1
        return

    for i in arr:
        total += i
        backtracking(total)
        total -= i


backtracking(0)

print(cnt)