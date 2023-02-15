def solution(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i]*b[i])
        
    return sum(result)