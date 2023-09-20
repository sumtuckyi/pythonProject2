
# N, M
# 연산한 결과는 1_000_000이하인 자연수여야한다.
# 최소연산횟수를 출력
# 매 연산의 결과를 큐에 삽입하고 꺼내서 또 연산
# from collections import deque
#
#
# def bfs(v):
#     visited = set()
#     queue = deque([(v, 0)])
#     while True:
#         now, cnt = queue.popleft()
#         if now == M:  # 큐에서 꺼낸 값이 목표일 때
#             return cnt
#         if now in visited:
#             continue
#         visited.add(now)
#         if now <= 999_999:
#             queue.append((now + 1, cnt + 1))
#         if now >= 2:
#             queue.append((now - 1, cnt + 1))
#         if now <= 500_000:
#             queue.append((now * 2, cnt + 1))
#         if now >= 11:
#             queue.append((now - 10, cnt + 1))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     print(f'#{tc} {bfs(N)}')

from collections import deque


def bfs(v):
    visited = set()
    queue = deque([(v, 0)])
    while True:
        now, cnt = queue.popleft()
        if now == M:  # 큐에서 꺼낸 값이 목표일 때
            return cnt
        if now in visited:
            continue
        visited.add(now)
        if now <= 999_999:
            queue.append((now + 1, cnt + 1))
        if now >= 2:
            queue.append((now - 1, cnt + 1))
        if now <= 500_000:
            queue.append((now * 2, cnt + 1))
        if now >= 11:
            queue.append((now - 10, cnt + 1))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')