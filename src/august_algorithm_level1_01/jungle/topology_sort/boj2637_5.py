# https://campkim.tistory.com/10
import sys
from collections import deque
input=sys.stdin.readline
#입력값 받기 
N=int(input()) #부품 수 N이 완제품
V=int(input()) #간선 수
E=[[] for _ in range(N+1)] #연결정보.
indegree=[0]*(N+1) #부품별 진입차수 0일 경우 기본부품.
needs=[[0]*(N+1) for _ in range(N+1)] #각 부품이 기본부품 얼마나 필요한지 Matrix

for i in range(V):
    a,b,c = map(int,input().split())
    E[b].append([a,c])  #a만드는데 b가 c개 필요.
    indegree[a]+=1      #진입차수 정보모음

q=deque()
basic_parts=[]
for i in range(1,N+1):
    if indegree[i]==0:
        basic_parts.append(i) #기본부품 리스트
        q.append(i)

while q:
    now=q.popleft()
    for object, n in E[now]:
        if now in basic_parts:   # 기본부품일경우 목적제품에 +n개
            needs[object][now]+=n
        else:
            for i in range(1,N+1):
                needs[object][i]+=needs[now][i]*n
        indegree[object]-=1
        if indegree[object]==0:
            q.append(object)

for i in range(N+1):
    if needs[N][i] > 0:
        print(i,needs[N][i])

#위랑 같은 표현
# for x in enumerate(needs[N]):
#     if x[1]>0:
#         print(*x)