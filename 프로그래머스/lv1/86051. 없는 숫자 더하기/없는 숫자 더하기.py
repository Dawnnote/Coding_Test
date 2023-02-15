def solution(numbers):
    result = 0
    for i in range(1, 10):
        if i not in numbers:
            result += i
            
    return result
            