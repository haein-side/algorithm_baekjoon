import sys
sys.setrecursionlimit(10**6)

#입력받을 원소 리스트
num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num)
    except:
        break

def postorder(left,right):
    #순서 역전시 종료
    if left>right:
        return
    else:
        for i in range(left+1,right+1): # 루트 노드인 left 노드를 빼고 right 노드 인덱스까지 돎
            
            #현재 원소가 루트 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
            #현재 원소 이후(이상)는 오른쪽 서브 트리이다.
            
            if num_list[left] < num_list[i]: # num_list[left]: 루트 노드 | num_list[i]: 현재 노드
                mid=i # 오른쪽 서브트리 노드의 인덱스
                break
        else:
            mid=right+1 
            # 오른쪽 서브트리의 가장 큰 원소의 인덱스
            # 오른쪽 서브트리가 없을 경우를 대비한 것
            
        postorder(left+1,mid-1) # left 인덱스는 루트 노드이므로 left+1 인덱스부터 해줘야
        postorder(mid,right) 
        print(num_list[left]) # 루트 노드 출력

postorder(0,len(num_list)-1)