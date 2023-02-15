def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot [1] < 0:
        return 3
    else:
        return 4
    
    
#     a, b = 1, 0
    
#     if dot[0]*dot[1] > 0:
#         b = 1
#     elif dot[1] < 0:
#         a = 2
        
#     return 2*a-b