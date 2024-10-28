def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i] in ['1','2','3','4','5','6','7','8','9']:
            answer += int(my_string[i])
    
    return answer