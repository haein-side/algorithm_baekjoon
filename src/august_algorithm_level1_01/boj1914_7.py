import sys
a = int(sys.stdin.readline())
count = 0

# 하노이탑 이동 흔적 보기
def hanoi(n, start, goal, via):
    if n == 1:
        print(str(start) + " " + str(goal))
        return
    
    hanoi(n-1, start, via, goal)
    
    print(str(start) + " " + str(goal))
    
    hanoi(n-1, via, goal, start)

# 하노이탑 이동 횟수를 세기 위한 함수
# n-1개의 원반을 2번 옮기고, 제일 아래 원반은 1번 옮김
def moveCount(n):
    if n == 1: # 원반이 한 개 남았을 때는 한번만 옮기면 됨
        return 1
    return 2 * moveCount(n-1) + 1

print(moveCount(a))
hanoi(a, 1, 3, 2)

