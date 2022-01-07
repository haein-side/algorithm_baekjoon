# 고정 길이 큐 FixedQueue 구현하기

from typing import Any

class FixedQueue:
    
    class Empty(Exception) :
        pass
    
    class Full(Exception) :
        pass
    
    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
        
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity  # self.capacity는 큐의 크기
    

# 실습4-3 (enque)
    def enque(self, x:Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        
        if self.rear == self.capacity:
            self.rear = 0
            # rear에 하나 더한 값이
            # capacity와 동일해지면 넣은 후에 rear의 인덱스를 0으로 수정
            # 그 다음에 인큐하는 데이터가 인덱스 0에 제대로 저장됨
            
# 실습 4-4 (deque)
    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x


            

    