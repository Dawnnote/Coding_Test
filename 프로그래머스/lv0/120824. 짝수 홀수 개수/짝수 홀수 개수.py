def solution(num_list):
    result = []
    even_num = 0
    odd_num = 0
    
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even_num += 1
        else:
            odd_num += 1
            
    result.extend([even_num, odd_num])
            
    return result
