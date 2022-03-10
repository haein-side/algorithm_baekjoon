import sys
T = int(sys.stdin.readline())
arr = []

for i in range(T):
    data = sys.stdin.readline().strip() # strip()을 가지고 문자열 맨 앞과 맨 끝의 공백문자를 제거
    A, B = data.split()
    arr.append([i+1, int(A), B])

b = sorted(arr, key = lambda x:(x[1], x[0]))

for i in range(len(b)):
    print(b[i][1], b[i][2])
