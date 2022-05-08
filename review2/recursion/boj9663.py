# N-Queen
# 대각선 조건 고려 X
import sys
input = sys.stdin.readline

n = int(input())
# pos[열] = 행
pos = [0 for _ in range(n)] # 각 열의 어느 행에 뒀는지 확인
flag = [False for _ in range(n)] # 각 행에 뒀는지 확인

'''
처음에 각 행에 뒀는지 확인하는 flag를 선언할 때
flag = [False * n]으로 뒀었다.
그러나 이 경우 * 연산자를 사용하여 얕은 복사가 실행되기 때문에
flag를 프린트해보면 [0]이 출력된다.
따라서 flag를 False 여러개를 가진 배열로 프린트하기 위해 
flag = [False for _ in range(n)]으로 하면 여러 개의 원소가 출력된다.
얕은 복사를 피하기 위해 for문을 사용하면 해결된다!
'''

def place(col): # 매개변수는 어느 열에 뒀는지
    count = 0
    if col == n: # 열의 끝까지 뒀으면
        return 1 # 1개의 경우의 수 반환
    
    for i in range(n):
        if not flag[i]: # 아직 안 놓은 행이면
            pos[col] = i # set열 i행에 위치시킴
            flag[i] = True
            count += place(col+1)
            flag[i] = False
    
    return count

# 0열부터 시작
print(place(0)) # 대각선 조건 고려하지 않을 때는 40320이 출력됨
