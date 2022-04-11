import sys
# 스택의 제일 위의 값과 넣을 값을 비교하며 
# 넣을 값이 클 경우 스택의 제일 위의 값을 제거
# 반복하며 넣을 값이 작아질 경우 스택에 넣어줌

# 제일 큰수로 만들려면 앞에 있는 작은 수부터 제거해야

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip()))
answer = []
delNum = k

for i in range(n):
    while delNum > 0 and answer: # delNum > 0이고 stack에 값이 있을 때동안 현재 자신보다 작은 게 stack에 남아있으면 모두 pop해줌
        if answer[len(answer)-1] < nums[i]:
            answer.pop()
            delNum -= 1
        else: # stack에 있는 값이 나보다 크면 그대로 두고 break 
            break
    answer.append(nums[i]) # 그 전꺼가 나보다 작은지 큰지 비교하고 내꺼 넣어주기 // 더이상 delNum > 0이 아니면 계속 append

for i in range(n-k):
    print(answer[i], end="")
    