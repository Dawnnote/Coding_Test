def solution(slice, n):
    result = 0
    
    if (n%slice) == 0:
        result = n//slice
    else:
        result = (n//slice)+1
            
    return result