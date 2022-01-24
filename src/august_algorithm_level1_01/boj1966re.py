import sys

t = int(sys.stdin.readline())

for i in range(t):
    N, M = map(int, input().split())
    
    n = list(map(int, input().split()))
    idx = list(range(len(n)))
    idx[M] = 'target'
    
    if N == 0 :
        print(1)
    else :
        count = 0
        while True :
            if n[0] < max(n):
                n.append(n[0])
                n.pop(0)
                idx.append(idx[0])
                idx.pop(0)
            else:
                if idx[0] == 'target' and n[0] == max(n) :
                    count += 1
                    print(count)
                    break
                else :
                    n.pop(0)
                    count += 1
                    idx.pop(0)
                # if target == max(list):
                #     print("target", target)
                #     print(count)
                        
        

# https://assaeunji.github.io/python/2020-05-04-bj1966/