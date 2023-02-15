def solution(n):
    lis = []
    result = 0
    
    for i in range(2, n+1):
        for j in range(1, i+1):
            
            if i % j == 0:
                lis.append(i)
                
        if lis.count(i) >= 3:
            result += 1
            
    return result