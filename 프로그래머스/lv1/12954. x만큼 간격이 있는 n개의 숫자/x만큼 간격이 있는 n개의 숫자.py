def solution(x, n):
    answer = []
    try:
        for i in range(x,x*(n+1),x):
            answer.append(i)
    except:
        answer = [0]*n
    
    return answer
        