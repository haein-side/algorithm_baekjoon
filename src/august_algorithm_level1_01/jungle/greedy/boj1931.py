import sys
input = sys.stdin.readline

n = int(input())
meet = [[0, 0] for _ in range(n)]

for i in range(n):
    meet[i] = list(map(int, input().split()))
    
meet.sort(key = lambda x: (x[1], x[0])) # 두번째 원소순(종료시간) 정렬, 같으면 첫번째 원소순(시작시간) 정렬
# 3
# 3 3
# 1 1
# 2 3
# [[1, 1], [2, 3], [3, 3]] | x[0]을 안 해주면 3이 아니라 2가 출력됨

sch = [0] # 할 수 있는 회의의 종료시간을 넣어두는 배열

for i in range(n):
    if sch[-1] <= meet[i][0]: # 마지막 회의 종료시간 <= 회의 시작시간
        sch.append(meet[i][1]) # 해당 회의 종료시간 넣기

print(len(sch)-1)
