import re

def solution(babbling):
    patterns = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for word in babbling:
        pattern = '^(' + '|'.join(patterns) + ')+$'
        if re.match(pattern, word):
            result += 1
    
    return result


import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt
