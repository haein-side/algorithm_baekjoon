def solution(numbers):
    sum = []
    
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            sum.append(numbers[i] + numbers[j])
    
    sum = set(sum)
    answer = sorted(sum)
    
    return answer