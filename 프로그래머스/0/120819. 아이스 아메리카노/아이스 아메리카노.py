def solution(money):
    answer = [0,0]
    answer[0] = money // 5500
    answer[1] = money - (5500 * answer[0])
    return answer


def solution(money):

    answer = [money // 5500, money % 5500]
    return answer
