from sys import stdin

input = stdin.readline

n = int(input())
nodes = {} # 이진 트리 노드

# 딕셔너리 자료구조를 이용하여 이진 트리 구현
for _ in range(n):
    m_node, l_node, r_node = input().strip().split() # m_node : 루트 노드, l_node : 좌측 자식 노드, r_node : 우측 자식 노드
    nodes[m_node] = {'left':l_node, 'right':r_node}

# 전위 순회 : (루트) (왼쪽 자식) (오른쪽 자식)    
def preorder(root = 'A'):
    if root == ".":
        return
    
    print(root, end="")
    preorder(nodes[root]['left'])
    preorder(nodes[root]['right'])

# 중위 순회 : (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(root = 'A'):
    if root == ".":
        return
    
    inorder(nodes[root]['left'])
    print(root, end="")
    inorder(nodes[root]['right'])

# 후위 순회 : (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(root = 'A'):
    if root == ".":
        return
    
    postorder(nodes[root]['left'])
    postorder(nodes[root]['right'])
    print(root, end="")

preorder()
print()
inorder()
print()
postorder()