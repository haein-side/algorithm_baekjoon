import sys
input = sys.stdin.readline
 
n, r, c = map(int, input().split())
 
# n: 변의 길이,x: 현재 위치의 x축 값, y:현재 위치의 y축 값
result = 0
def N(n, x, y):
    global result
 
    if x==r and y==c: # 현재 위치와 목표 지점이 같을 때
        print(int(result))
        exit(0) # 문제 없이 깨끗한 출구를 의미
 
    if n == 1: # 2*2가 사분면의 최소 단위라서 2*2일 때 result에 각 사분면마다 1씩 더해줌
        result += 1
        return # 함수 중간에서 빠져나옴
 
    if not(x<=r<x+n and y<=c<y+n): # 해당 사분면에 원하는 위치가 없으면
        result += n*n # 해당 사분면에 원하는 위치가 없으므로 반으로 나뉜 n*n을 result에 더해줌
        return # return 값은 없고 result라는 global 변수에 값을 계속 더해줌!
        # 해당 사분면 안에 값이 없으면 바로 재귀 끝나고 돌아가줌 (더이상 n/2를 안해줌)
        # 해당 사분면 안에 값이 있으면 이 부분에서 재귀가 끝나는 게 아니라 계속 n/2로 나눠줌 until n == 1
 
    # 만약 해당 사분면에 값이 존재하면 위의 if로 들어가지 않아서 return이 안 됨! (즉, 재귀가 끝나지 않은 상태)
    # 그러면 바로 1사분면으로 내려가서 변의 길이를 1/2해주고 
 
    # 1사분면
    N(n/2, x, y)
    # 2사분면
    N(n/2, x, y+n/2)
    # 3사분면
    N(n/2, x+n/2, y)
    # 4사분면 (현재의 정사각형에서 1/2를 해서 4분면인 부분의 시작점을 잡아줌 as x+n/2, y+n/2)
    N(n/2, x+n/2, y+n/2)
 
N(2**n, 0, 0)