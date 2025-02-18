# 강사님 코드
def solution(n):
    answer = 0
    while n > 0:
        a, b = divmod(n, 10) # divmod() = (몫, 나머지) 출력해줌
                                # ,로 두개 값 할당 시, a = 몫, b = 나머지 할당됨
    # 나머지의 누적합 구하기
    answer = answer + b
    n = a # while문 돌릴 때 1234 처음에 했으면, 다음에 나눠서 나머지 구해야 하는 건 몫인 123이기 때문
    return answer
print(solution(1234))

# 두번째 방식
def solution(n):
    answer = 0
    # for문으로는 시퀀스만 돌릴 수 있음, 숫자는 못 함 >> 그럼 str(n)으로 감싸기 >> 그럼 '1234'의 문자열로 변환하는 것
    for i in str(n):
        answer = answer + int(i) # 문자열로 변환했던 것을 다시 정수형으로 바꾸기
    return answer
print(solution(1234))
print(solution(930211))

# 3. map(): return sum(map(int, list(str(n))))
def solution(n):
    