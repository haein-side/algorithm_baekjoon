def solution(arr):
    answer = []
    answer.append(arr[0])
    w = arr[0]
    for i in range(1, len(arr)):
        if w != arr[i]:
            w = arr[i]
            answer.append(w)
                
    return answer
        
print(solution([1,1,3,3,0,1,1]))