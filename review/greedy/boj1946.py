import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    staff = []
    for _ in range(n):
        staff.append(list(map(int, input().split())))
        
    staff.sort()
    res = 1 # 서류 1등은 무조건 합격이므로 1을 넣어두고 시작
    cri = staff[0][1] # 서류 1등의 면접 등수
    for i in range(1, n):
        score = staff[i][1]
        if cri > score:
            res += 1
            cri = score
    
    print(res)