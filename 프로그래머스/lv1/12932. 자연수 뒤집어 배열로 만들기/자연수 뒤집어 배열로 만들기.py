def solution(n):
    N = str(n)
    result = []
    
    for i in N:
        result.append(int(i))
        
    return list(reversed(result))