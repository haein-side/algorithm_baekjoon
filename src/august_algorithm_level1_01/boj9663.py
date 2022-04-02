import sys

n = int(sys.stdin.readline())

pos = [0] * n
f_a = [False] * n
f_b = [False] * (2*n-1)
f_c = [False] * (2*n-1)

c = 0

def set(i, n):
    global c
    for j in range(n):
        if ( not f_a[j]            # j행에 퀸이 배치 되지 않았다면
            and not f_b[i + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not f_c[i - j + (n-1)]):
            pos[i] = j  # 퀸을 j행에 배치
            if i == n-1:  # 모든 열에 퀸을 배치하는 것을 완료
                c += 1
               
            else:
                f_a[j] = f_b[i + j] = f_c[i - j + (n-1)] = True
                set(i + 1, n)  # 다음 열에 퀸을 배치
                f_a[j] = f_b[i + j] = f_c[i - j + (n-1)] = False
            
    return c

print(set(0, n))