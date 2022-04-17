import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
maxNum = -99999
minNum = 99999

def dfs(depth, total, plus, minus, multi, divide):
    global maxNum, minNum
    
    if depth == N: # ex. 연산자 1개, N 2개 : 연산자 1개 고르면 끝나야 하므로 depth가 2가 되면 return 시켜서 재귀 종료
        # if depth == N 없을 경우, 연산자 N-1개 이하로 골랐을 때 연산 결과가 그대로 minNum과 maxNum에 저장됨
        # 따라서 연산자를 N개 골랐을 때에만 아래 코드가 작동하도록 해야함!
        maxNum = max(maxNum, total)
        minNum = min(minNum, total)
        return
    
    if plus > 0:
        dfs(depth + 1, total + num[depth], plus-1, minus, multi, divide)
     
    if minus > 0:
        dfs(depth + 1, total - num[depth], plus, minus-1, multi, divide)
    
    if multi > 0:
        dfs(depth + 1, total * num[depth], plus, minus, multi-1, divide)
    
    if divide > 0:
        if total < 0:
            moc = (-total) // num[depth]
            total = -moc
        else:
            total = total // num[depth]
        dfs(depth + 1, int(total), plus, minus, multi, divide-1)
    
    
dfs(1, num[0], plus, minus, multi, divide)

print(maxNum)
print(minNum)