def solution(array, n):
    num = 0 
    for i in array:
        if i == n:
            num = num + 1
    return num