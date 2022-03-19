def solution(arr):
    answer = []
    for i in range(0, len(arr)-2):
        if arr[i] == arr[i+1]:
            # answer.append(arr[i])
            continue
        else:
            if len(answer) > 0 and answer[len(answer)-1] != arr[i]: 
                answer.append(arr[i])
                answer.append(arr[i+1])
            else:
                answer.append(arr[i+1])
                
    answer[0]
        
    return answer
        