def solution(left, right):
    result = []
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i%j == 0:
                cnt += 1
        
        if cnt%2 == 1:
            result.append(-i)
        else:
            result.append(i)

                    
    return sum(result)
                