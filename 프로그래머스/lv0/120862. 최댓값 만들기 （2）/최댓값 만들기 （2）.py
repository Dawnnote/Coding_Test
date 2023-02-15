def solution(numbers):
    result = numbers[0] * numbers[1]
    
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
            if numbers[i] * numbers[k] > result:
                result = numbers[i] * numbers[k]
            
    return result