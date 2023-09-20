# 0~9
# make-set
# 부모 노드를 저장
parent = [i for i in range(10)]

# find-set
def find_set(x):
    if parent[x] == x:
        return x

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    # 이미 같은 집합인지 확인
    x = find_set(x)
    y = find_set(y)
    if x == y:
        print("cycle")
        return
    # 같은 집합이 아니라면
    # ★트리의 height를 rank로 삼아 rank가 낮은 집합을 큰 집합에 이어 붙인다.
    if x < y:  # 값이 작은 노드를 대표로
        parent[y] = x
    else:
        parent[x] = y


union(0, 1)
union(2, 3)
union(1, 3)

# 이미 같은 집합인 요소를 합치면, cycle이 발생
union(0, 2)

print(find_set(2))
print(find_set(3))

t_x = 0
t_y = 2
if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합')
else:
    print('다른 집합')

