import sys

t = int(sys.stdin.readline())

for i in range(t):
    N, M = map(int, input().split())
    
    n = list(map(int, input().split()))
    target = n[M]
    
    if N == 0 :
        print(1)
    else :
        count = 0
        while True :
            if target == max(n) :
                count += 1
                print(count)
                break
            else:
                if n[0] < max(n):
                    n.append(n[0])
                    n.pop(0)
                    # print(list)
                else:
                    n.pop(0)
                    count += 1
                    # if target == max(list):
                    #     print("target", target)
                    #     print(count)
                        
        

# https://assaeunji.github.io/python/2020-05-04-bj1966/