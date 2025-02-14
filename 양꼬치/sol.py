# 내가 작성한 코드
def solution(n, k):
    if n >= 10:
        k = k - int(n / 10)
    answer = (12000 * n) + (2000 * k)
    return answer

print(solution(10, 3))
print(solution(64, 6))

#강사님 코드
def solution(n, k):
    if n >= 10:
        service = n // 10
        answer = (12000 * n) + (2000 * (k-service))
    else:
        answer = (12000 * n) + (2000 * k)
    return answer
print(solution(10, 3))
print(solution(64, 6))

# 코드 압축하기
def solution(n, k):
    # 양꼬치 + 음료수 - 서비스가격
    answer = (12000 * n) + (2000 * k) - (n // 10 * 2000)