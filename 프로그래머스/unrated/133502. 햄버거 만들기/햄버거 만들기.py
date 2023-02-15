def solution(ingredient):
    buger = [1, 2, 3, 1]

    idx = 0
    result = 0
    while idx < len(ingredient)-3:
        if ingredient[idx] == 1:
            if ingredient[idx:idx+4] == buger:
                del ingredient[idx:idx+4]
                result += 1
                idx -= 3
        idx += 1
            
    return result

    
#     buger = '1231'

#     str_ingredient = "".join(str(n) for n in ingredient)

#     result = 0
#     while True:
#         if buger in str_ingredient:
#             str_ingredient = str_ingredient.replace(buger, '', 1)
#             result += 1
            
#         if buger not in str_ingredient:
#             break
            
#     return result