# M=2 중복인 경우 : 순서는 다르지만 같은 조합인 경우
# M=3 중복인 경우 : 이미 나왔던 번호가 나온 경우도 중복으로 처리, 아예 모두 다른 눈금이 나와야함
# 주사위를 던진 횟수는 2이상 5이하(6이면 M=3일 때 가능한 경우가 1부터 6까지 골고루 나온 경우 뿐이기 때문)
N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]


# M=1인 경우 :N번 던졌을 때 나올 수 있는 모든 경우
def backtracking(level, path):
    if level == N:
        print(*path)
        return

    for num in dice:
        backtracking(level+1, path + [num])


# M=2인 경우
def backtracking2(level, path, check):
    if level == N:
        if check in checked:
            return
        else:
            checked.append(check.copy())
            print(*path)
            return

    for num in dice:
        check[num] += 1
        backtracking2(level+1, path + [num], check)
        check[num] -= 1


# M=3인 경우
def backtracking3(level, path):
    if level == N:
        print(*path)
        return

    for num in dice:
        if check[num] == 0:
            check[num] = 1
            backtracking3(level+1, path + [num])
            check[num] = 0


check = [0]*7
checked = []
if M == 1:
    backtracking(0, [])
elif M == 2:
    backtracking2(0, [], check)
elif M == 3:
    backtracking3(0, [])

'''
M=2에서 중복을 제거하는 다른 방법
if level > 0 and i < path[level-1]:
    continue
'''