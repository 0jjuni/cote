def solution(dot):
    answer = 0
    x, y = dot[0], dot[1]
    if x > 0:
        if y > 0:
            answer = 1
        else:
            answer = 4
    else:
        if y > 0:
            answer = 2
        else:
            answer = 3
    return answer