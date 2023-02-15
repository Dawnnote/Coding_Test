def solution(my_str, n):
    num = n
    
    result = []
    k = 0
    a = len(my_str)//num
    
    while True:
        result.append(my_str[k:n])
        
        n += num
        k += num
        
        if n > len(my_str):
            break
    
    result.append(my_str[k:])
    
    if "" in result:
        result.remove('')
        
    return result