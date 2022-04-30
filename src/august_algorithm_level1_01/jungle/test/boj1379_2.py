# https://www.acmicpc.net/problem/1379
# 접근 방법
# 강의 정보를 강의 시간을 기준으로 정렬한다.
# 강의 정보를 반복문을 통해 하나씩 확인한 뒤, 해당 강의의 종료시간과 강의실 번호를 힙에 넣는다. 
# 이때 힙에 저장되어있는 종료 시간 중, 현재 탐색 중인 강의의 시작시간보다 작거나 같은 경우 모두 뺀다.
# 매 탐색마다 힙의 길이만큼의 인덱스에 해당하는 것을 강의실 번호로 매겨 이를 강의실 번호를 기준으로 하는 리스트에 저장한다.
# 또한 각 강의실 중 비어있는 위치는 강의실에 대한 minHeap을 통해 구한다.

import sys, heapq
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lecture = [0 for _ in range(n+1)]
arr.sort(key=lambda x: (x[1], x[2]))

room = [] # 방의 숫자 (배정 가능한 애들을 다 넣어줌)
# room에 i를 넣음
for i in range(1, n+1):
    heapq.heappush(room, i)

minHeap = [] # 비교대상이 될 가능성이 있는 애들을 다 넣어줌
for x in arr:
    while minHeap and minHeap[0][0] <= x[1]: # 계속 뽑힘 (종료시간 <= 현재 회의의 시작시간)
        end, r = heapq.heappop(minHeap) # end 가 가장 작은 것만 계속 뽑아내줌
        heapq.heappush(room, r) # 그 방에 다시 배정해줄 수 있으므로 가능성 있는 애들을 다시 room에 넣어줌

    r = heapq.heappop(room) # 조건 맞는 애들 중 가장 작은 애만 뽑아줌
    heapq.heappush(minHeap, [x[2], r]) # 끝나는 시간이 달라지므로 또 minHeap에 넣어줌 (비교대상 또 되게)
    lecture[x[0]] = r # 종료시간과 강의번호 같이 minHeap에 넣어주기

print(max(lecture))
for x in lecture[1:]:
    print(x)