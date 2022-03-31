import sys

def sol(n):
    a = n[0]
    score = []
    for i in range(1, a+1):
        score.append(n[i]) 
    med = sum(score) / a
    count = 0
    for i in score:
        if i > med:
            count += 1
            
    bi = round(count/a, 5) # 반올림에 round() 함수 이용 - 뒤에 인수는 몇째자리까지 나오느냐 
    return str(f'{bi*100:.3f}')+"%" # 5자리까지 나와야 100배 곱해 주었을 때 소수점 세자리까지 나옴
    # 소수점 셋째자리까지 나오게 소수점 자리수를 제한해줄 수 있음
    
              

c = int(sys.stdin.readline())

for i in range(c):
    nlist = list(map(int, sys.stdin.readline().split()))
    print(sol(nlist))
    