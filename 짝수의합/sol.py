# 내가 작성한 코드
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 != 0 :
            continue
        else:
            answer = answer + i
    return answer

print(solution(10))
print(solution(4))

# 강사님 코드
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0 :
            answer = answer + i
    return answer

def solution(n):
for i in range(2, n+1, 2):
    return sum(i)
print(solution(10))
