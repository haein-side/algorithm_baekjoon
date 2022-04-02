import sys

def hanoi(n, start, destination, via):
    m = ''
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        m += str(start) + " " + str(destination) + "\n"
        return 1

    count = 0
 
    count += hanoi(n - 1, start, via, destination) 

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    count += 1
    m += str(start) + " " + str(destination) + "\n"

    count += hanoi(n - 1, via, destination, start) # hanoi 에서 리턴한 1들을 하나씩 count에 저장함

    return m, count


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    start = 1
    destination = 3
    via = 2

    c = hanoi(n, start, destination, via)
    
    print('총 이동 횟수:', c)