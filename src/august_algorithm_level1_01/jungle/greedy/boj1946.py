# 시간초과 -> 기준 갱신
import sys

input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 지원자 숫자
    
    score = [[0, 0] for _ in range(n+1)]
    
    for i in range(1, n+1):
        score[i] = list(map(int, input().split()))
    
    score.sort() # 서류순 오름차순 정렬
    
    res = n 
    cri =  score[1][1] # 서류 1등 면접 등수
    for i in range(2, n+1):
        if score[i][1] > cri: # 현재 면접순위가 나보다 서류순위 높은 것의 면접순위보다 작아야 하므로 (크면 합격 안됨)
            res -= 1
        else:
            cri = score[i][1] # 현재 면접순위가 나보다 서류순위 높은 것의 면접순위보다 작으면 나의 면접순위로 기준 갱신 
    
    print(res)