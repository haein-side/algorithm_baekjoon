import sys

n = int(sys.stdin.readline())
arr = [[0 for col in range(n)] for i in range(n)]

for i in range(n):
    word = sys.stdin.readline()
    for j in range(n):
        arr[i][j] = word[j]

zerocnt = 0 # 0의 개수
onecnt = 0 # 1의 개수
answer = ""

before = n//2
tmp = 0
def sol(n, x, y): # n : 현재 변의 길이, x: 현재 좌표 행 위치, y: 현재 좌표 열 위치
    global answer
    
    zerotmp = 0
    onetmp = 0
    
    for i in range(n): # n이 4일 때 0, 1, 2, 3
        for j in range(n): # n이 4일 때 0, 1, 2, 3
                if arr[x+i][y+j] == "0":
                    zerotmp += 1
                else:
                    onetmp += 1
    
    if zerotmp == n*n: # 0으로만
        answer = answer + "0"
        return
    elif onetmp == n*n: # 1로만
        answer = answer + "1"
        return 
    else:
        answer += "(" # 재귀를 돌리는 부분에 괄호를 주면 됨
        sol(n//2, x, y)
        sol(n//2, x, y + n//2)
        sol(n//2, x + n//2, y)
        sol(n//2, x + n//2, y + n//2)
        answer += ")"
    
sol(n, 0, 0)

print(answer)