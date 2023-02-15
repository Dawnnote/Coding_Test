def solution(n):
    lis = list(range(1,n+1))
    result = []
    
    for i in range(len(lis)):
        if n%lis[i] == 0:
            result.append(lis[i])
    
    return sum(result)