def solution(dots):
    xdots = [dot[0] for dot in dots]
    ydots = [dot[1] for dot in dots]
    
    return (max(xdots)-min(xdots)) * (max(ydots)-min(ydots))