def solution(n):
    answer = 0
    n = [n]
    for i in n:
        answer = answer + i
    return answer

print(solution(1234))
