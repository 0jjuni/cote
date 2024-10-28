def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        temp = rsp[i]
        if temp == '2':
            answer += '0'
        elif temp == '0':
            answer += '5'
        else:
            answer += '2'
    return answer