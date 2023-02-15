def solution(n):
    result = 0
    for i in range(n):
        result += 1
        
        while result % 3 == 0 or '3' in str(result):
            result += 1
        
    return result