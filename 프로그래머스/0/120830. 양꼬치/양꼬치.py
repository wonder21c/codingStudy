def solution(n, k):
    service = 0
    yang = n * 12000
    coke = k * 2000
    service = (n // 10) * 2000
    
    answer = yang + coke - service
    return answer