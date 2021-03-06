MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"


def move(N, start, destination):
    print(MOVE_MESSAGE.format(N, start, destination))


def hanoi(n, start, destination, via):
    """
    하노이의 탑 규칙에 따라 원반을 옮기고,
    옮길 때마다 원반의 시작 위치와 이동한 위치를 출력합니다.
    마지막으로 총 이동 횟수를 반환합니다.
    :params
        n: 총 원반 개수
        start: 시작 기둥
        destination: 도착 기둥
        via: 보조 기둥:
    :return count:
    """
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        move(1, start, destination)
        return 1

    count = 0
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
    # 원반을 옮길 때 한번에 한개씩만 옮길 수 있으므로 원반이 1개만 남을 때까지 계속 재귀를 실행
    # 마침내 원반이 1개만 남았을 때 1을 리턴해주는 것
    count += hanoi(n - 1, start, via, destination) # hanoi 에서 리턴한 1들을 하나씩 count에 저장함

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    count += 1
    move(n, start, destination)

    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동
    # 원반을 옮길 때 한번에 한개씩만 옮길 수 있으므로 원반이 1개만 남을 때까지 계속 재귀를 실행
    # 마침내 원반이 1개만 남았을 때 1을 리턴해주는 것
    count += hanoi(n - 1, via, destination, start) # hanoi 에서 리턴한 1들을 하나씩 count에 저장함

    return count


if __name__ == '__main__':
    n = 3
    start = 1
    destination = 3
    via = 2

    total_count = hanoi(n, start, destination, via)
    print('총 이동 횟수:', total_count)


'''
출력 결과

1번 원반을 1에서 3로 이동
2번 원반을 1에서 2로 이동
1번 원반을 3에서 2로 이동
3번 원반을 1에서 3로 이동
1번 원반을 2에서 1로 이동
2번 원반을 2에서 3로 이동
1번 원반을 1에서 3로 이동
총 이동 횟수: 7
'''