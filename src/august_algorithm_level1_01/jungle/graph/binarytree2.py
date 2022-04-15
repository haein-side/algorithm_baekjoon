from sys import stdin

input = stdin.readline

n = int(input())
nodes = {}

# 딕셔너리 자료구조를 이용하여 이진 트리 구현
for _ in range(n):
    m_node, l_node, r_node = input().strip().split()
    nodes[m_node] = {'left':l_node, 'right':r_node}


def preorder(root='A'):
    if root == '.':
        return

    print(root, end='')
    preorder(nodes[root]['left'])
    preorder(nodes[root]['right'])

def inorder(root='A'):
    if root == '.':
        return
    
    inorder(nodes[root]['left'])
    print(root, end='')
    inorder(nodes[root]['right'])

def postorder(root='A'):
    if root == '.':
        return

    postorder(nodes[root]['left'])
    postorder(nodes[root]['right'])
    print(root, end='')

preorder()
print()
inorder()
print()
postorder()