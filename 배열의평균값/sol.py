# 내가 작성한 코드
def solution(numbers):
    answer = sum(numbers)/len(numbers)
    return answer
    # 압축할 수 있음: return sum(numbers)/len(numbers)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(numbers))

numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(solution(numbers))

# 강사님 코드

def solution(numbers):
   total = 0 #누적합 통해 총합 구하기
   i = 0 #길이
   for num in nums:
        total = total + num
        i = i + 1
    answer = total / i
    return answer
print(total, i)
