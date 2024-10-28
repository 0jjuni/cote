def solution(sides):
    max = 0
    for i in sides:
        if max < i:
            max = i
    if sum(sides) - 2 * max > 0:
        answer = 1
    else:
        answer = 2
    return answer