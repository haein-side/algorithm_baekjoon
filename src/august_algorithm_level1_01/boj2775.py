import sys

def solve(num1, num2):
    floor_0 = [i for i in range(1, num2 + 1)]
    
    print(floor_0)
    
    for i in range(num1):
        for j in range(1, num2):
            floor_0[j] += floor_0[j-1]
            print(j, floor_0[j-1], floor_0[j])
    
    return floor_0[-1]


T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    print(solve(k,n))