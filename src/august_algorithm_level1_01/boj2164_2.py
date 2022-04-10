import sys
import collections

n = int(sys.stdin.readline())
card = [i for i in range(1,n+1)]
d = collections.deque(card)

while len(d) >= 1:
    d.popleft()
    if len(d) == 1:
        print(d[0])
        break
    elif len(d) == 0:
        print(1) # 카드가 한 장 남았을 때 남은 카드를 출력해야 하므로 1을 pop 한 다음에는 1을 출력해줌
        break
    a = d.popleft()
    d.append(a)
