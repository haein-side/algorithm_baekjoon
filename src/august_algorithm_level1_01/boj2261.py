import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# x좌표 기준으로 정렬
arr = sorted(arr)

def distance(dot1, dot2):
    d = (dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2
    return d

def main(start, end):
    mid = (start + end) // 2
    
    # 점이 하나가 남았을 때
    if start == end:
        return float('inf')
    # 점이 두개가 남았을 때
    if end - start == 1:
       return distance(arr[start], arr[end])
   
    left = main(start, mid)
    right = main(mid+1, end)
    
    # left와 right로 구역 나눴을 때 최솟값
    mindis = min(left, right)

    # 타겟리스트
    tl = []
    # 가운데 구역에서의 거리 보기
    for i in range(start, end+1): # 재귀를 돌리고 인덱스 기준으로 봐야 하므로 len(arr)이 아닌 것!
        if (arr[mid][0] - arr[i][0])**2 < mindis: # mindis 보다 작아야 함
            tl.append(arr[i])
    
    # y를 기준으로 정렬
    tl = sorted(tl, key = lambda x: x[1])
    
    L = len(tl)
    # y 좌표 기준으로 먼저 보고,
    # 그 다음에 좌표 간의 거리 비교해서 최소 거리 구하기
    for i in range(L-1):
        for j in range(i+1, L):
            if (tl[i][1] - tl[j][1])**2 >= mindis: # mindis보다 y좌표 값들 간 거리가 크거나 같으면 더이상 볼 필요가 없음!
                break
            else:
                mindis = min(distance(tl[i], tl[j]), mindis)
    
    return mindis
     
    
    

print(main(0, N- 1))


