# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

while True :
    n = input()
    
    if n == "0":
        break
    
    if n == n[::-1]:
        answer = "yes"
    else :
        answer = "no"
    print(answer)