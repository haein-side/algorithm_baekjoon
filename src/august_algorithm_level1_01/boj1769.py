import sys

n = sys.stdin.readline().strip()
answer = 0
count = 0

def sol(n):
    global answer, count
    if len(n) == 1 :
        if n in ['3', '6', '9']:
            answer = "YES"
        else:
            answer = "NO"
        return
    
    count += 1
    a = 0 # 각 자리 숫자의 합
    for i in range(len(n)):
        a += int(n[i])
    
    sol(str(a))

sol(n)
print(count)
print(answer)
