# 1번 - 중위 / 2번 - 전위 / 3번 - 후위
# 왼쪽부터 채워진 트리가 아님 -> 왼쪽은 비어있지만 오른쪽이 채워진 경우에는 오른쪽을 출력해야함
def inorder(v):
    if v == -1:
        return
    inorder(lights[v][1])
    print(v, end=' ')
    inorder(lights[v][2])


def preorder(v):
    if v == -1:
        return
    print(v, end=' ')
    preorder(lights[v][1])
    preorder(lights[v][2])


def postorder(v):
    if v == -1:
        return
    postorder(lights[v][1])
    postorder(lights[v][2])
    print(v, end=' ')


N = int(input())
lights = [[] for _ in range(N+1)]
for _ in range(N):
    row = list(map(int, input().split()))
    lights[row[0]].extend(row)
inorder(1)
print()
preorder(1)
print()
postorder(1)