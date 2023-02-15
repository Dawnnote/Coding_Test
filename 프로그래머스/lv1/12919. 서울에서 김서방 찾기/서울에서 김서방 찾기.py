def solution(seoul):
    gps = -1
    kim = "Kim"
    
    for i in seoul:
        gps += 1
        if i == kim:
            return f"김서방은 {gps}에 있다"
        