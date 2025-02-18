# 1. 오름차순 정렬해 큰 수 2개 뽑기
def solution(numbers):
   numbers.sort()
   return numbers[-1] * numbers[-2]

#print(solution([1, 2, 3, 4, 5]))

# 2. 직접 sort 원리를 코드로 짜보기
def solution(numbers):
   n = len(numbers) # 1~5까지의 길이 들어감
   for i in range(n):
      for j in range(0, n-i-11):
         if numbers[j] > numbers[i+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j] # 두 숫자 비교해서 더 큰 숫자는 오른쪽으로 옮기는 것
   return numbers[-1] * numbers[-2]
print(solution([1, 2, 3, 4, 5]))

# sort는 이런 원리로 작동함: 버블 알고리즘으로 큰 수 비교해서 오름차순으로 정렬하는 식임: 버블 sort는 앞에서부터 2개 숫자 비교해서 큰 수 오른쪽으로 미룸 >> 그럼 큰 수인 오른쪽부터 정렬 이뤄짐
# 퀵 sort: 반으로 코드 나눠서 앞뒤 동시에 정렬하는 식 >> 그래서 속도 빠름
