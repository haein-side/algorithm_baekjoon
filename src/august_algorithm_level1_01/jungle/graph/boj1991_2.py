import sys

n = int(sys.stdin.readline())
nodes = {} # 이진 트리 노드

for i in range(n):
    a, b, c = sys.stdin.readline().split()
    nodes[a] = [b, c] # node[루트][0] : 좌측 자식 노드 | node[루트][1] : 우측 자식 노드

# 전위 순회 : (루트) (왼쪽 자식) (오른쪽 자식)    
def preorder(root = 'A'):
    if root == ".":
        return
    print(root, end = "")
    preorder(nodes[root][0])
    preorder(nodes[root][1])

# 중위 순회 : (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(root = 'A'):
    if root == ".":
        return
    inorder(nodes[root][0])
    print(root, end = '')
    inorder(nodes[root][1])
    
# 후위 순회 : (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(root = 'A'):
    if root == '.':
        return
    postorder(nodes[root][0])
    postorder(nodes[root][1])
    print(root, end='')    
    
preorder()
print()
inorder()
print()
postorder()