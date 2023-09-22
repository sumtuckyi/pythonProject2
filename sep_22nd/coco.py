from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 업무의 수
    data = []  # 노드와 간선 정보 저장
    t = [0]  # 0번째 비움, 해당 업무만 처리하는데 걸리는 시간
    for i in range(N):
        task = list(map(int, input().split()))
        data.append(task)
        t.append(task[0])
    d = [0] * (N + 1)  # 진입차수 초기화, 0번째 비움
    adj_lst = [[] for _ in range(N + 1)]  # 인접리스트(진출차수 저장), 0번째 비움
    # adj_lst2 = [[] for _ in range(N+1)]  # 사전업무 저장
    result = 0
    for i in range(N):
        if data[i][1] != 0:  # 진입차수가 0이 아닌 노드인 경우
            d[i + 1] = data[i][1]  # 진입차수 저장
            for j in range(2, 2 + data[i][1]):
                adj_lst[data[i][j]].append(i + 1)  # 진출차수 저장, data[i][j]번째 업무가 처리되어야 i+1번째 업무를 처리 가능
                # adj_lst2[i+1].append(data[i][j])  # 해당 업무의 사전업무 저장

    coco = []
    path = []
    # 모든 경우의 수 탐색
    for k in range(N):
        path = []
        origin = t[k + 1]
        t[k + 1] = t[k + 1] // 2  # k번째 작업을 코코가 도와주는 경우
        dp = [0] * (N + 1)
        temp = d.copy()  # 진입차수, 모든 작업이 종료되면 리스트의 값은 전부 0이 되어야 한다.
        q = deque()
        for i in range(1, N + 1):
            if not temp[i]:  # 진입차수가 0인 노드를 모두 큐에 삽입
                q.append(i)
                dp[i] = t[i]  # 사전업무가 없는 작업의 경우 작업에 걸리는 최소시간
        while q:
            cur = q.popleft()  # 해당 노드에서 나가는 간선을 제거(해당 업무를 처리)
            path.append(cur)  # 업무 처리 순서를 확인하기 위한 리스트
            if adj_lst[cur]:  # 현재 노드가 처리되어야 진행될 수 있는 작업 존재시
                adj_lst[cur].sort()  # 작업들을 오름차순 정렬
                for e in list(adj_lst[cur]):  # 각 작업들에 대해
                    temp[e] -= 1  # 진입차수를 1 빼고(사전작업 중 하나를 처리)
                    dp[e] = max(dp[cur] + t[e], dp[e])  # 각 작업이 완료되기까지의 시간을 기존의 최소시간과 비교하여 갱신
                    if temp[e] == 0:  # e번 업무의 사전업무가 모두 처리된 경우
                        q.append(e)
        # 큐가 비었는데 아직 처리되지 않은 일들이 남은 경우 -> 사이클 존재
        if len(set(temp)) != 1:
            result = -1
            break
        coco.append(max(dp))
        t[k + 1] = origin
    # print(f'#{tc} {coco}')

    ans = result if result == -1 else min(coco)
    print(f'#{tc} {ans}')
