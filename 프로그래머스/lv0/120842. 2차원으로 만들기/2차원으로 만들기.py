def solution(num_list, n):
    result = []
    i = 0
    num = n
    
    while True:
        result.append(num_list[i:n])
        
        n += num
        i += num
        
        if n > len(num_list):
            break
            
    return result