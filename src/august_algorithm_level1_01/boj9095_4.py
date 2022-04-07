import sys

t = int(sys.stdin.readline())
count = 0 
def sol(n):
    global count
    if n == 0:
        count += 1
    if n < 0:
        return
    for i in range(1, 4): # 1부터 3까지 선택
        sol(n-i) # 리턴값만 영향을 받는다! // 위에서 아래로 코드는 실행됨!
    

for i in range(t):
    sol(int(sys.stdin.readline()))
    print(count)
    count = 0