def solution(word):
    answer = 0
    words = ["A", "E", "I", "O", "U"]

    for i in range(len(word)):
        # 길이가 i인 단어의 개수: 5^(i+1) - 1 / 4
        cnt = (5**(i+1) - 1) // 4
        # 이전 단어의 개수만큼 더함
        answer += cnt

        # word와 사전에서 앞선 단어를 찾기
        if word[i] in words:
            # 현재 글자의 인덱스를 찾음
            idx = words.index(word[i])
            # 현재 길이에서 word의 다음 글자까지의 모든 단어의 개수를 더함
            answer += idx * (5**(len(word)-i-1))

    return answer
    
print(solution("AAAAE"))  # 6
print(solution("AAAE"))  # 10
print(solution("I"))  # 1563
print(solution("EIO"))  # 1189
