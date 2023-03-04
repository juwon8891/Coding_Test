def getFinalString(s):
    final_string = str(s) # 입력 문자열을 문자열로 변환합니다.
    while "AWS" in final_string: # "AWS" 문자열이 있는 동안 반복합니다.
        final_string = final_string.replace("AWS", "") # "AWS" 문자열을 제거합니다.
    if final_string == '': # 만약 결과 문자열이 비어 있다면
        return '-1' # -1을 문자열로 반환합니다.
    return final_string # 그렇지 않으면 결과 문자열을 반환합니다.

# 이 코드는 주어진 문자열 s에서 "AWS" 문자열을 모두 제거하고 결과 문자열을 반환합니다. 이를 위해 while 루프를 사용합니다.
# while "AWS" in final_string: 은 "AWS" 문자열이 final_string 문자열에 있는 동안에 반복합니다. 
# 반복할 때마다 final_string 문자열에서 "AWS" 문자열을 replace 함수로 제거합니다.
# 그리고 만약 결과 문자열이 비어 있다면, -1을 문자열로 반환합니다. 그렇지 않으면 결과 문자열을 반환합니다.

s = "AAWSWS"
# s = "AAWSWS"
print(getFinalString(s))