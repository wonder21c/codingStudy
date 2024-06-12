def solution(cipher, code):
    answer = ''
    cnt = 1
    for i in cipher:
        if cnt % code == 0:
            answer += i
        cnt = cnt + 1
    return answer

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
