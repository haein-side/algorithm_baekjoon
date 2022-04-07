import sys
count = 0
def sol(n, one, two, three):
    global count
    print(one, two, three)
    
    h = one*1 + two*2 + three*3
    
    if one < 0 or two < 0 or three < 0:
        return
    
    if h == n:
        count += 1
        print(count)
        # return
    if h > n:
        return
    
    if one >= 0 and three == 0:
        sol(n, one-2, two+1, three)
    # print(n, one, two, three)
    # newThree = n // 3 + 1
    # newOne = n % 3 + 1
    sol(n, one%3+1-1, two+2, one//3+1-1)
    # sol(n, newOne-2, two+1, newThree-1)
    # sol(n, newOne-1, two+2, newThree-1)   


t = int(sys.stdin.readline())

for i in range(t):
    a = int(sys.stdin.readline())
    sol(a, a, 0, 0)
