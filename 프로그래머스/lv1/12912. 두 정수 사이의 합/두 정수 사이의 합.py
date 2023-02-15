def solution(a, b):
    answer = []
    
    if a > b:
        a, b = b, a
        
    for i in range(a, b+1):
        answer.append(i)
        
    return sum(answer)