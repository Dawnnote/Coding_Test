def solution(price, money, count):
    S = sum([price*i for i in range(1, count+1)])-money
    return 0 if S <= 0 else S
    
    
    