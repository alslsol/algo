def solution(my_string, letter):
    result = []
    for char in my_string:
        if char != letter:
            result.append(char)
    return ''.join(result)
print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))