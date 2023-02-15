def solution(sides):
    s_num = max(sides) - min(sides)
    b_num = max(sides) + min(sides)
    
    return (b_num - s_num) - 1