import sys

def solution(n: int):
    return search([0] * n, 0)


def search(queen: list, row: int):
    n = len(queen)
    count = 0

    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        if check(queen, row):
            count += search(queen, row + 1)
            
    return count


def check(queen: list, row: int):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False # 방문할 수 없으면 False

    return True # 방문할 수 있으면 True

n = int(sys.stdin.readline())
print(solution(n))