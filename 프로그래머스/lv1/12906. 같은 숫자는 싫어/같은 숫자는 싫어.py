def solution(arr):

    num_lis = []

    for i in range(len(arr)):
        if num_lis[-1:] == [arr[i]]:
            continue
        num_lis.append(arr[i])
        
    return num_lis