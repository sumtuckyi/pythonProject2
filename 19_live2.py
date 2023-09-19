# 트리 자료구조 구현하기
'''
5개의 간선
1 2 1 3 2 4 3 5 3 6
'''

'''
1. 1차원 배열 : [1, 2, 3, 4, 0, 5, 6]
i번 노드의 값 = 배열의 i번째 인덱스 위치의 값
2. 연결리스트 :

3. 인접리스트 :
'''
# 연결리스트로 구현
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        return
    # 전위순회
    def preorder(self):
        if self:
            print(self.value, end=' ')
            # 왼쪽 자식노드가 있다면
            if self.left:
                self.left.preorder()
            # 오른쪽 자식노드가 있다면
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value, end=' ')


# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()
print()
nodes[1].inorder()
print()
nodes[1].postorder()

# 2차원배열로 구현
nodes = [[] for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

# 자식이 더 이상 없다는 것을 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(v):
    if v == None:
        return

    print(v, end=' ')
    preorder(nodes[v][0])
    preorder(nodes[v][1])
def inorder(v):
    if v == None:
        return

    inorder(nodes[v][0])
    print(v, end=' ')
    inorder(nodes[v][1])

def postorder(v):
    if v == None:
        return

    postorder(nodes[v][0])
    postorder(nodes[v][1])
    print(v, end=' ')


print()
preorder(1)
print()
inorder(1)
print()
postorder(1)