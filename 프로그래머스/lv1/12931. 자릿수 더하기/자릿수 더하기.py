def solution(n):
    answer = 0
    N = str(n)
    
    for i in range(len(N)):
        answer += int(N[i])

    return answer
