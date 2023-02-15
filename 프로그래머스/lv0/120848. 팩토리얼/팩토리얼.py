def solution(n):
    i = 1
    while True:
        
        n = int(n/i)
        
        if n == 0 and n%i == 0:
            break
        result = i
        i += 1
        
    
    return result