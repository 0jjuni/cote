def solution(n):
    temp = n % 7
    if temp == 0:
        answer = n // 7
    else:
        answer = (n // 7) +1
    return answer