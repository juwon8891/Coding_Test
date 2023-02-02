def solution(k):
    answer = -1
    dic = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    if len(str(k)) == 1:
        answer = dic[k]
    else:
        answer = -1
    return answer


k = 9
print(solution(k))
