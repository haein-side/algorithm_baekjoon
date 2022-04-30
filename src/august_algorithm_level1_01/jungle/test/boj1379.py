import sys
input = sys.stdin.readline

n = int(input())
cl = []

for _ in range(n):
    cl.append(list(map(int, input().split())))

cl = sorted(cl, key = lambda x : x[2]) # 종료 시간이 짧은순으로 정렬

gang = 1 # 강의실 수
glist = [cl[0][2]] # 각 회의실 별 강의가 끝나는 시간
clist = [] # 각 회의별 강의실 번호

for i in range(1, n): # 각 회의별로 따져줌
    flag = True
    for j in range(i): # 그 전에 존재하는 회의들과 비교
        for end in glist:
            if end <= cl[i][1]: # 종료시간 <= 현재 회의의 시작시간이면 해당 위치로 배정되어야
                glist[glist.index(end)] = cl[i][2] # glist에 현재 회의의 종료시간을 해당 위치에 넣어줌
                
                flag = False
                break
        if not flag:
            break
        else: # 종료시간 > 현재 회의 시작시간이면 새로운 위치로 배정되어야
            gang += 1
            glist.append(cl[i][2])
            break

# 필요한 강의실 개수
print(gang)