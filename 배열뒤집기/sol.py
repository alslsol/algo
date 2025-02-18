# 1. 슬라이싱 활용하기
def solution(num_list):
    result = num_list[::-1]
    return result
print(solution([1, 2, 3, 4, 5]))


# 2. reverse() 활용하기
def solution(num_list):
    num_list.reverse()
    return num_list
print(solution([1, 2, 3, 4, 5]))

# 3. 반복문
def solution(num_list):
    result = []
    for num in num_list:
        result.insert(0, num) # append는 뒤에 추가하는 식, insert는 내가 지정한 자리에 추가 가능 >> 0번째에 추가하겠단 것
    return result
print(solution([1, 2, 3, 4, 5]))
