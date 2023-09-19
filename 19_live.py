arr = [i for i in range(1, 4)]
path = [0] * 3


def backtracking(cnt):
    # 재귀호출을 중단할 조건
    if cnt == 3:
        print(*path)
        return
    # 경우의 수를 줄이기 위한 추가적인 조건(option)

    # 반복문
    for num in arr:
        # ★★★가지치기 - 중복된 숫자 제거★★★
        if num in path:
            continue
        # 재귀함수를 호출하기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀함수 호출
        backtracking(cnt + 1)
        # ★★★돌아와서 할 로직★★★
        path[cnt] = 0


backtracking(0)