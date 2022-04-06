import sys

t = int(sys.stdin.readline().strip())
nlist = [int(sys.stdin.readline()) for i in range(t)]
slist = [False, False] + [True] * 10002 # slist[i]가 i를 가리키게 하도록 0부터 값 부여

# 10000까지 소수 리스트 생성
for i in range(2, 10001):
    if i == 1:
        continue
    
    for j in range(2, int(i**0.5)+1):
        if i % j == 0: 
            slist[i] = False # 소수가 아니기 때문에 False
            break
    else:
        slist[i] = True # 소수이므로 True
        
def check(n):
    f = n//2
    s = f
    while f > 0: # 이렇게 조건 주는 게 좋음!
        if slist[f] and slist[s]:
            print(str(f) + " " + str(s))
            break
        else:
            f -= 1
            s += 1


for i in nlist:
    check(i)