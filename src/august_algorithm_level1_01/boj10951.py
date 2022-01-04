while True :
    try:
        n = list(map(int,input().split()))
        print(n[0] + n[1])
    except:
        break
    
# try - except 사용해야 함
# try에 대한 에러가 발생한 경우 while문을 멈춤 by break