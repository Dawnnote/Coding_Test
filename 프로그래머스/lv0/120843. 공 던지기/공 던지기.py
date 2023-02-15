def solution(numbers, k):
    num_lis = numbers * k
    result = num_lis[::2]
    
    return result[k-1]