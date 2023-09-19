# 무게가 같다면 황금이 돌보다 먼저 나옴
# import heapq
#
# n = int(input())
# bars = list(map(int, input().split()))
# heapq.heapify(bars)
# # check_g = [0]*10000
# # check_s = [0]*10000
# for bar in bars:
#     check_g[bar] += 1
# cnt = 0
# while bars:
#     # 첫 번째로 가벼운 물건 꺼내기
#     first = heapq.heappop(bars)
#     if check_g[first] >= 1:  # 꺼낸 물건이 황금이면
#         check_g[first] -= 1
#         cnt += 1
#         print(first)
#     else:  # 짱돌이면
#         break
#     # 두 번째로 가벼운 물건 꺼내기
#     fake = heapq.heappop(bars)
#     if check_g[fake] >= 1:
#         check_g[fake] -= 1
#         cnt += 1
#         print(fake)
#     else:
#         break
#     # 짱돌 넣기
#     heapq.heappush(bars, fake*2)
#     print(fake*2)
#     print('cnt:', cnt)
# print(cnt)

#
import heapq
N = int(input())  # 황금의 개수
arr = list(map(int, input().split()))
que = []  #황금과 짱돌을 저장할 최소 힙
cnt = 0  #황금의 개수
for i in range(N): #입력받은 황금의 무게들을 최소 힙(que)에 추가
    heapq.heappush(que, [arr[i], -1]) # 각 황금의 무게와 -1(황금을 의미)을 저장
while que: #힙에 요소가 있을때 까지 반복
    x, tp = heapq.heappop(que) # 1. 힙에서 가장 가까운 돌을 꺼낸다.
    if tp == 0: #꺼낸돌이 짱돌이면
        break
    cnt += 1 #황금을 꺼냈으므로 cnt += 1

    y, tp = heapq.heappop(que) #2. 다음 가장 가벼운 돌을 꺼낸다
    if tp == 0:
        break
    else: #꺼낸돌이 황금이면
        heapq.heappush(que, [y*2, 0]) #황금의 2배의 무게의 짱돌을 힙에 추가
    cnt += 1 #황금을 꺼냈으므로 cnt += 1
print(cnt)