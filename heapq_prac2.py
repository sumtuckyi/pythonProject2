import heapq

# N = int(input())  # 사람 수
# d = [500]
# heapq.heapify(d)
# for _ in range(N):
#     a, b = map(int, input().split())
#     heapq.heappush(d, a)
#     heapq.heappush(d, b)
#
# while heapq:
#     print(heapq.heappop(d))


# 다른 풀이
import heapq

max_heap = []  # mid보다 작은 값
min_heap = []  # mid보다 큰 값
mid = 500

def push(v):
    # 입력받은 값이 기준값보다 작은 경우
    if mid > v:
        # v의 절댓값이 클수록 작은 값이 되므로 가장 먼저 출력된다.
        heapq.heappush(max_heap, -v) #max heap을 구현을 위해 -1을 곱해준다
    # 입력받은 값이 기준값보다 큰 경우
    else:
        heapq.heappush(min_heap, v)


n = int(input())  # 점수가 추가되는 케이스의 수
for _ in range(n):
    a, b = map(int, input().split()) # 점수는 매번 2개씩 추가됨
    push(a)
    push(b)
    # mid보다 작은 값의 개수가 큰 값의 개수보다 많은 경우 -> mid값을 갱신해야하는데 이때 새로운 mid값은 max_heap(길이가 더 긴 배열)에서 가장 큰 값이 된다
    if len(max_heap) > len(min_heap):
        # 기존 mid값을 큰 값 배열(길이가 더 짧은 배열)에 추가
        heapq.heappush(min_heap, mid)
        # 작은 값 배열에서 가장 큰 값을 새로운 mid값으로 설정한다.
        mid = -heapq.heappop(max_heap) #max heap에서 값을 꺼낼때 -1을 곱해준다
    # mid보다 큰 값의 개수가 작은 값의 개수보다 많은 경우 -> 새로운 mid값을 min_heap에서 가장 작은 값으로 정해준다.
    elif len(max_heap) < len(min_heap):
        # 기존 mid값을 작은 값 배열에 추가
        heapq.heappush(max_heap, -mid) #max heap에 값을 넣을때 -1을 곱해준다
        # 큰 값 배열에서 가장 작은 값을 새로운 mid값으로 설정한다.
        mid = heapq.heappop(min_heap)
    print(mid)

