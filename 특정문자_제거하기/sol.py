def solution(my_string, letter):
    result = []
    for char in my_string:
        if char != letter:
            result.append(char)
    return ''.join(result)
print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))

# 강사님 코드
def solution(my_string, letter):
    answer = my_string.replace(letter, '') # letter를 비어있는 문자열로 바꿀거란 것
                                # 근데 스트링 메소드는 원본 수정 않으므로 따로 연산 결과 저장해놔야 함
    return answer
print(solution("abcdef", "f"))