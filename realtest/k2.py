queue1 = [1, 1]
queue2 = [1, 5]

def solution(queue1, queue2):
    from collections import deque

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    maxcnt = 2 * len(queue1)
    cnt = 0

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while sum1 != sum2:
        if cnt > maxcnt + 1:
            return -1

        if sum1 < sum2:
            queue1.append(queue2.popleft())
        elif sum1 > sum2:
            queue2.append(queue1.popleft())

        cnt += 1

        sum1 = sum(queue1)
        sum2 = sum(queue2)
    
    return cnt

print(solution(queue1, queue2))