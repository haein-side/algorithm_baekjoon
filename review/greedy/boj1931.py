import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))

# 종료 시간이 같을 때는 최대 회의 갯수를 위해서는 시작 시간이 빠른 거 먼저 채워넣기 ex. [2, 5] [5, 5] 의 경우
meeting = sorted(meeting, key = lambda x : (x[1], x[0])) 

end = meeting[0][1]
res = 1
for i in range(1, n):
    if end <= meeting[i][0]:
        end = meeting[i][1]
        res += 1

print(res)