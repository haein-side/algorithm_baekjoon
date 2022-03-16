from sys import stdin
from collections import deque

n = int(stdin.readline())

deq = deque()

def sol(word):
    arr = word.split()
    x = arr[0]
    if x == "push_front":
        return deq.appendleft(arr[1])
    elif x == "push_back":
        return deq.append(arr[1])
    elif x == "pop_front":
        try: return deq.popleft()
        except: return -1
    elif x == "pop_back":
        try: return deq.pop()
        except: return -1
    elif x == "size":
        return len(deq)
    elif x == "empty":
        if deq: return 0
        else: return 1
    elif x == "front":
        try: return deq[0]
        except: return -1
    elif x == "back":
        try: return deq[len(deq)-1]
        except: return -1

for i in range(n):
    word = stdin.readline().strip()
    answer = sol(word)
    if answer != None:
        print(answer)
    
    
    
