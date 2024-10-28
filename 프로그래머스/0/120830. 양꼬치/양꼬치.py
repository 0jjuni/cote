def solution(n, k):
    if n >= 10:
        answer = n * 12000 + 2000 * (k - n//10)
    else:
        answer = n * 12000 + 2000 * k
    return answer