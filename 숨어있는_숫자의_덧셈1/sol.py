# 1. 강사님 코드
def solution(my_string):
    numbers = [] # 숫자만 뽑아 저장할 리스트 공간 만들기

    for char in my_string:
        if char.isdigit(): # 해당 캐릭터가 숫자인지 묻기: is~ 메소드: 참/거짓 판별해줌 | isdigit(): 해당 캐릭터가 숫자인지 판별해줌
            numbers.append(int(char))
    return sum(numbers)

print(solution("aAb1B2cC34oOp"))

# 2. 아스키 코드 활용한 방식
# 함수 ord("문자열"): 문자열 입력 시, 아스키 코드에서의 index 위치 알려줌
    # 알파벳: 65 ~ 122, 숫자: 48~57
def solution(my_string):
    answer = 0
    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')): # 대문자 A부터, 소문자 z까지, char이 알파벳이 아닌가요를 묻는 것 >> not 붙이면 부정
            answer += int(char)
    return answer
print(solution("aAb1B2cC34oOp"))


# 3. 쉬운 방법
def solution(my_string):
    answer = 0
    numbers = '0123456789'
    for char in my_string:
        if char in numbers:
            answer += int(char)
    return answer
print(solution("aAb1B2cC34oOp"))

# 4. try-except 활용하기
def solution(my_string):
    answer = 0
    for char in my_string:
        try: # 아래 코드를 일단 문제 있든 없든 시도해보란 것 >> 문제 없음 넘어가고, 문제 있으면 넘어가라고 하는 식
            answer += int(char) # 근데 글자는 int() 하면 에러 >> 에러 나는 경우는 continue
        except:
            continue
    return answer
print(solution("aAb1B2cC34oOp"))