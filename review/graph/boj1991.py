import sys

N = int(sys.stdin.readline())
graph = {} # 이진 트리 노드 : 계속 해당 루트 값을 찾아서 꼬리를 물고 들어가야 하므로 딕셔너리 자료구조 사용
for i in range(N):
    a, b, c = sys.stdin.readline().split()
    graph[a] = (b, c) # 루트 : [좌측 노드, 우측 노드]


def preorder(root = 'A'):
    if root == '.': # 해당 루트값이 . 이면 더이상 자식노드가 없는 것이므로 리턴
        return
    print(root, end = '')
    preorder(graph[root][0])
    preorder(graph[root][1])

def midorder(root = 'A'):
    if root == '.':
        return
    midorder(graph[root][0])
    print(root, end = '')
    midorder(graph[root][1])

def postorder(root = 'A'):
    if root == '.':
        return
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root, end = '')

preorder()
print()
midorder()
print()
postorder()