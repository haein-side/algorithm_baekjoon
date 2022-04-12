# while문으로 이진탐색 구현
def bsearch(target, data):
    # data 중에서 target을 찾는 것
    data.sort()
    start = 0
    end = len(data)-1
    # mid = (start + end) // 2 (X)
    
    while start <= end:
        mid = (start + end) // 2  
        # mid는 if문 대소비교로 바뀌는 start, end의 값에 따라 계속 갱신되어야 하므로
        # while문 안에 있어야 함
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
    
    return None # target이 없으면 whlie문 빠져 나오므로 None을 리턴

target = 0
data = [1,2,3]
# 재귀로 이진탐색 구현
# 힌트 : 재귀함수의 매개변수에는 start, end, target, data가 들어간다
def bsearch2(start, end, target, data):
    if start > end: # 재귀 종료 조건
        return None
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    elif data[mid] < target:
        start = mid + 1
    
    return bsearch2(start, end, target, data) # 리턴을 안 해주면 마지막에 값을 가져올 수가 없음
 
data.sort()   
bsearch2(0, len(data)-1, target, data)
