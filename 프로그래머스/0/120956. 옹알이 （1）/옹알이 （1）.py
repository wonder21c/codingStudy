import re

def solution(babbling):
    patterns = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for word in babbling:
        
        pattern = '^(' + '|'.join(patterns) + ')+$'
        
        
        if re.match(pattern, word):
            result += 1
    
    return result
