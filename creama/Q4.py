def longestChain(words):
    n = len(words)
    dp = {word: 1 for word in words}  # 모든 단어의 초기 최장 체인 길이는 1입니다.
    words.sort(key=len)  # 단어를 길이가 작은 순서대로 정렬합니다.
    max_chain_length = 1  # 최장 체인 길이를 1로 초기화합니다.
    
    for i in range(n):
        for j in range(len(words[i])):
            word = words[i]
            reduced_word = word[:j] + word[j+1:]
            if reduced_word in dp:
                dp[word] = max(dp[word], dp[reduced_word] + 1)
        max_chain_length = max(max_chain_length, dp[word])
    
    return max_chain_length

word = ['a', 'and', 'an', 'bear']
word = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
print(longestChain(word))

# words 리스트를 len 함수를 기준으로 정렬합니다. 이는 나중에 체인을 형성할 때 가장 긴 체인을 형성할 가능성이 높은 단어부터 시작할 수 있도록 합니다.
# max_chain_length를 1로 초기화합니다. 이 변수는 이전에 찾은 최장 체인 길이를 저장합니다.
# for 루프를 사용하여 각 단어에 대한 가능한 모든 체인을 찾습니다. i는 단어 목록에서 인덱스를 나타내고, j는 해당 단어의 각 문자를 나타냅니다.
# 현재 단어를 word에 할당하고, 한 문자가 제거된 단어를 reduced_word에 할당합니다.
# 이 단어가 dp에 있다면, 현재 단어 word의 체인 길이는 이전 체인 길이(dp[word])와 한 문자가 제거된 단어의 체인 길이(dp[reduced_word] + 1) 중 더 큰 값이 됩니다.
# max_chain_length를 현재 단어 word의 체인 길이와 비교하여 더 큰 값을 max_chain_length에 할당합니다.
# 이렇게 함으로써 이전에 찾은 최장 체인 길이를 유지하고, 
# 이전보다 더 긴 체인이 나타났을 때만 max_chain_length를 업데이트할 수 있습니다.
# max_chain_length를 반환합니다. 이 값은 주어진 단어 목록에서 찾을 수 있는 가장 긴 체인의 길이입니다.