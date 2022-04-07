# 3
# 백준 1182
# 정글 A반 2조 이주형
import sys
N, S = map(int, sys.stdin.readline().strip().split()) # N: 숫자 개수, S: 원하는 수의 합
A = list(map(int,sys.stdin.readline().strip().split())) # 리스트
cnt = 0
def make_subsequence(now, Idx): # now: 현재 리스트, Idx: 현재 인덱스
    global S, cnt
    n = len(A)
    if Idx == n: # 종료조건 이유 => 입력받은 리스트의 길이와 Idx가 같아진다는 것은 이제 전체 함수의 길이를 초과한다는 뜻이므로
        if sum(now)==S and now: # 현재 리스트의 합이 S이고 now 현재 리스트가 0이 아니어야 함
            cnt +=1
        return
    now.append(A[Idx]) # 입력받은 리스트의 Idx 인덱스 원소를 현재 리스트에 append시켜줌
    make_subsequence(now,Idx+1)
    now.pop()
    make_subsequence(now,Idx+1)
make_subsequence(list(), 0)
print(cnt)