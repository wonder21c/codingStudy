def solution(n):
    if n == 1:
        return [[1]]
    answer = [[0 for i in range(n)] for i in range(n)]
    a = 0
    b = 0
    start = "r"
    for i in range(n*n):
        answer[a][b] = i + 1
        if start == "r":
            b += 1
            if b == n - 1 or answer[a][b+1] != 0:
                start = "d"
        elif start == "d":
            a += 1
            if a == n - 1 or answer[a+1][b] != 0:
                start = "l"
        elif start == "l":
            b -= 1
            if b == 0 or answer[a][b-1] != 0:
                start = "u"
        elif start == "u":
            a -= 1
            if a == 0 or answer[a-1][b] != 0:
                start = "r"       
            
    return answer
