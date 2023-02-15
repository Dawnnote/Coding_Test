def solution(x):
    X = str(x)
    arr = 0
    for i in X:
        arr += int(i)
    
    if x%arr == 0:
        return True
    
    return False