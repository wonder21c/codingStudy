def solution(array):
    max_value = max(array)   
    index_value = array.index(max_value)
    answer =[max_value, index_value]
    return answer