def solution(dots):
    for dt1, dt2, dt3, dt4 in [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]:
        dot1, dot2, dot3, dot4 = dots[dt1], dots[dt2], dots[dt3], dots[dt4]
        if (dot1[1]-dot2[1]) * (dot3[0]-dot4[0]) == (dot3[1]-dot4[1]) * (dot1[0]-dot2[0]):
            return 1
    return 0