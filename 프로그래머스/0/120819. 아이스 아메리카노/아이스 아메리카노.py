def solution(money):
    cof = money // 5500
    re = money -cof * 5500
    answer = [cof, re]
    return answer