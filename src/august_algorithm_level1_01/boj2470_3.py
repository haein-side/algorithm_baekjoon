import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

w.sort()
left = 0
right = n - 1
answer = w[left] + w[right] # 처음에는 가장 작은 수와 가장 큰 수를 더한 합을 answer로 넣어둠
al = left
ar = right

while left < right:
    tmp = w[left] + w[right] # "현재 left와 right의 합"인 tmp와 기존의 최솟값인 answer를 비교해서 최솟값을 계속 갱신해주는 것
    if abs(tmp) < abs(answer): # 기존 answer보다 "현재 left와 right의 합"인 tmp 가 작을 때 최솟값을 갱신
        answer = tmp # 현재 합인 tmp를 answer에 넣어줌
        al = left
        ar = right
        if answer == 0: # 만약 합이 0이 되면 break 해줌
            break
    
    if tmp < 0:
        left += 1 # 합이 음수이면 음수의 절댓값이 양수의 절댓값보다 큰 것이기 때문에 left += 1
    else:
        right -= 1 # 합이 양수이면 양수의 절댓값이 음수의 절댓값보다 큰 것이기 때문에 right -= 1
    
print(w[al], w[ar])
        