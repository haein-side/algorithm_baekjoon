import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

numlist = []
while True: # 막혔던 부분 try-except
    try:
        numlist.append(int(input()))    
    except:
        break

# root = numlist[0]
# left_g = []
# right_g = []
# for i in range(1, len(numlist)):
#     if numlist[i] < root:
#         left_g.append(numlist[i])
#     elif numlist[i] > root:
#         right_g.append(numlist[i])

# 전위순회된 리스트의 루트 노드들을 기준으로
# 원소들의 인덱스를 가지고 좌측서브트리 -> 우측서브트리 -> 루트 순으로 후위순회 시켜주는 것
def postorder(left, right):
    if left > right:
        return
    else:
        for i in range(left+1, right+1):
            if numlist[left] < numlist[i]: # 루트보다 큰 노드가 나오면 mid를 갱신
                mid = i
                break
        else:
            mid = right + 1
            
        postorder(left+1, mid-1)
        postorder(mid, right)
        print(numlist[left]) # left를 루트 노드로 생각!
    
postorder(0, len(numlist)-1)