def solution(n):
    num = 2
    lis = []
    result = []
    
    while num <= n:
        if n % num == 0:
            lis.append(num)
            n /= num
        else:
            num += 1
    
    for i in lis:
        if i not in result:
            result.append(i)
    
    return result