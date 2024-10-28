import numpy as np

def solution(array):
    temp = np.array(array)
    answer = np.median(temp)
    
    return answer

solution([1,2,7,10,11])