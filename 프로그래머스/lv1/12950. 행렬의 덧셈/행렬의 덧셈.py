def solution(arr1, arr2):
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
        
    return arr1

#     lis = []
#     s = []
    
#     for a, b in zip(arr1, arr2):
#         lis = []
#         for c, d in zip(a, b):
#             lis += [(c+d)]
#         s += [lis]
    
#     return s