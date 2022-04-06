import sys
sys.setrecursionlimit(10**7)
g, s = map(int, sys.stdin.readline().split())
count = 0
def sol(g, s):
    global count
    
    if g == s:
        count += 1
        return 
    
    a = min(g, s)
    if g > s:
        count += 1
        sol(g-a, s)
    
    if g < s:
        count += 1
        sol(g, s-a)
    
sol(g, s)
print(count)