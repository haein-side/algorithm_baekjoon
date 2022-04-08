from lib2to3.pgen2.token import LEFTSHIFTEQUAL
import sys
n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
w = sorted(w)
a = [] # 알칼리성 음의 정수
s = [] # 산성 양의 정수

al = 0 # left 인덱스
ar = 0 # right 인덱스

# 알칼리성과 산성을 분류
for i in w:
    if i < 0:
        a.append(i)
    elif i > 0:
        s.append(i)
a = sorted(a)
s = sorted(s)

if len(s) == 0 and len(a) > 0: # 음수인 것만 있을 때
    print(a[-2], a[-1])
elif len(a) == 0 and len(s) > 0: # 양수인 것만 있을 때
    print(s[0], s[1])
else: # 음수와 양수의 조합
    # 음수가 한 개이고 양수가 여러개
    if len(a) == 1 and len(s) > 1:
        al = 0
        ar = 1
        p = 0
        tmp = s[0] + s[1] # 양수인 것 두 개의 합
        for i in range(len(s)):
            if tmp > abs(a[0] + s[i]): # 음수 한 개와 양수 여러개들의 합이 양수 작은 것 두개의 합보다 작으면 업데이트
                tmp = abs(a[0] + s[i])
                al = 0
                ar = i
                p = 1
        # 프린트
        if p == 1:
            print(a[0], s[ar])
        elif p == 0:
            print(s[0], s[1])
        
    # 양수가 한 개이고 음수가 여러개
    elif len(s) == 1 and len(a) > 1:
        al = -2
        ar = -1
        p = 0
        tmp = abs(a[-2] + a[-1]) # 음수인 것 두 개의 합
        for i in range(len(a)):
            if tmp > abs(s[0] + a[i]): # 양수 한 개와 음수 여러개들의 합이 음수 작은 것 두개의 절댓값의 합보다 작으면 업데이트
                tmp = abs(s[0] + a[i])
                al = 0
                ar = i
                p = 1
        # 프린트
        if p == 1:
            print(a[ar], s[0])
        elif p == 0:
            print(a[-2], a[-1])
    
    elif len(s) == 1 and len(a) == 1:
        print(a[0], s[0])
    
    # 둘 다 여러 개
    else:
        left = 0
        right = len(w) - 1
        
        al = 0
        ar = 0
        tmp = float('inf')
        
        while left < right: # 용액은 모두 서로 다르기 때문에 left = right으로 인덱스가 같은 케이스는 포함시켜주면 안 됨!
            if tmp > abs(w[left] + w[right]):
                al = left
                ar = right
                tmp = abs(w[left] + w[right])
            
            if w[left] + w[right] == 0:
                al = left
                ar = right
                break
            elif w[left] + w[right] < 0:
                left += 1
            
            else:
                right -= 1
            
        print(w[al], w[ar])
                
