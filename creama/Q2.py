def findRange(num):
    max_val = num
    min_val = num
    
    # 0부터 9까지 루프를 돌면서 각 자리 숫자를 변환해본다
    for i in range(10):
        for j in range(10):
        # 입력된 숫자에서 i를 j로 변환해본다
            new_num = str(num).replace(str(i), str(j))
        # 새로운 숫자가 0으로 시작하지 않는 경우에만 고려
            if new_num[0] != '0':
                # 현재 최대값과 새로운 숫자 중에서 더 큰 값으로 최대값 갱신
                max_val = max(max_val, int(new_num))
                # 현재 최소값과 새로운 숫자 중에서 더 작은 값으로 최소값 갱신
                min_val = min(min_val, int(new_num))
    # 최대값과 최소값의 차이를 반환
    return max_val - min_val


# 코드의 동작 방식은 다음과 같습니다.
# num을 문자열로 변환합니다.
# 0부터 9까지의 숫자에 대해 다음을 반복합니다.
# num 문자열에서 현재 숫자와 같은 문자를 찾습니다.
# 만약 찾지 못했다면, 다음 숫자로 넘어갑니다.
# 찾은 경우, 현재 숫자를 0부터 9까지의 다른 숫자로 대체한 새로운 문자열 s를 생성합니다.
# s를 다시 숫자로 변환한 후, 이 값과 현재까지의 최소값, 최대값을 갱신합니다.
# 최대값과 최소값의 차이를 반환합니다.
# 즉, 가능한 모든 숫자 대체 경우의 수를 모두 시도해서 최소값과 최대값을 찾는 방법입니다.
# 이 알고리즘의 단점은 대체할 숫자가 많을수록 경우의 수가 기하급수적으로 증가한다는 것입니다.
# 따라서 입력값이 큰 경우에는 실행 시간이 오래 걸릴 수 있습니다.

print(findRange(123512) ) # 820082

# 이 코드는 잘못된 데이터 번역 함수에서 생긴 버그를 찾는 문제를 해결하는 코드입니다. 이 함수는 다른 시스템에서 온 일련의 숫자를 읽어들여 그것들을 해당 시스템의 지역 동등물로 변환합니다. 그러나 버그로 인해 숫자 중 하나가 잘못 변환됩니다. 예를 들어, 입력 데이터 값이 11891인 경우, 1 숫자와 관련된 버그가 있으며, 이를 지역 동등물로 9로 변환하면 함수는 99899를 반환합니다. 이 예시에서 원래 값의 9는 영향을 받지 않습니다. 이러한 가정하에 숫자 0~9 중 1개의 숫자가 잘못된다는 것을 알지 못하면, 가능한 최대 및 최소 값을 찾아낼 수 있습니다. 이 차이를 반환합니다.

# 이 함수는 입력값으로 받은 num 값의 각 자리수를 모두 0부터 9까지의 수 중 다른 값으로 변환하면서 이뤄지며, 변환된 결과를 이용하여 가능한 최대값과 최소값을 찾아서 둘의 차이를 반환합니다.

# 주어진 값 num에 대해, 가능한 모든 숫자 변환을 시도하여 가능한 최대값과 최소값을 찾습니다. 첫 자리 숫자는 0이 아닌 값이어야 하며, 유효한 숫자의 자릿수가 변하지 않도록 합니다. 최대값과 최소값의 차이를 반환합니다.