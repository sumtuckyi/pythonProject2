'''
가장 적은 비용으로 수영장을 이용할 수 있는 경우에 그 비용을 구하여라.
각기 다른 이용권의 종류와 가격이 주어짐


'''

def dfs(month, acc_cost):
    global ans

    if month > 12:
        ans = min(ans, acc_cost)

    if acc_cost > ans:
        return

    # 1일 이용권으로 그 달을 이용
    dfs(month + 1, acc_cost + (months[month]*cost_day))
