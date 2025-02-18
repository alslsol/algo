# 1. 쉽게 찾을 수 있는 방법
def solution(n):
    answer = 0
    for num in range(1, n+1):
        if n % num == 0: # 나머지 없는 경우 >> 약수 하나 찾은 것
            answer += 1

    return answer

print(solution(20))
# 약수 구하기인 셈

# 2. 효율적인 코드
#(1, 20) 있으면, (20, 1)은 당연히 있음 -> 절반까지만 나눴을 때 약수 있는지 확인해봐도 됨 -> 루트 n까지만 계산해도 됨
from math import sqrt # math의 루트 활용하기 위함
# 아니면, 루트 대신, int(n**0.5) 해서 1/2 승으로 해줄 수도 있음
def solution(n):
    answer = 0
    for num in range(1, int(sqrt(n)) + 1): # 루트 딱 떨어지지 않고 소수면 for문 안 돌아감 >> 정수로 바꾸기 위해 int(), 루트 씌우면 중앙값 자기 자신은 포함 안 되므로 +1 해준 것
        if n % num == 0:
            answer += 2 # 첫번째와 첫번째 뒤집힌 것 두개를 찾은 거나 다름 없기 때문에 2를 추가하는 것
            if num * num == n:
                answer -= 1 # 루트 씌운 게 n과 같은 같이면(ex. 10) 중복된 값 1개 빼겠단 것
    return answer
print(solution(20))

