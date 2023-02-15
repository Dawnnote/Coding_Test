def solution(chicken):
    result = 0
    add = 0
    c = 0
    
    while True:
        a = int(chicken/10)
        b = chicken%10
        result += a
        add += b
        chicken = a
        
        if add >= 10:
            result += int(add/10)
            add -= 10
            add += 1

        if a < 10:
            add += a
            break
            
    if add >= 10:
        result += int(add/10)
        
    return result