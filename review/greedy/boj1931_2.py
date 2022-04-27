import sys
input = sys.stdin.readline

n = int(input())
meeting = []

for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key = lambda x:(x[1], x[0]))
end = meeting[0][1]

res = 1
for i in range(1, n):
    if meeting[i][0] >= end: # 다음 회의 시작 시간 >= 끝나는 시간
        res += 1
        end = meeting[i][1]

print(res)
    
