def solution(my_string):
    result = ''
    for i in my_string:
        if i.isupper():
            result += i.lower()
        else :
            result += i.upper()
    return result


def solution(my_string):
    return my_string.swapcase()
