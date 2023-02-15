def solution(before, after):

    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    return 0
    
#     result_1 = {}
#     result_2 = {}
    
#     for i in before:
#         if i not in result_1:
#             result_1[i] = i
#         else:
#             result_1[i] += i
    
#     for i in after:
#         if i not in result_2:
#             result_2[i] = i
#         else:
#             result_2[i] += i
            
#     if result_1 == result_2:
#         return 1
#     else:
#         return 0