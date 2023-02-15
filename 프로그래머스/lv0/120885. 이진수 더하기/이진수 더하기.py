def solution(bin1, bin2):
    result = bin(int(bin1, 2)+int(bin2, 2))
    
    return result[2:]