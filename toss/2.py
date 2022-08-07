def solution(level):
    answer = []
    rank = int(len(level) * 0.25) + 1
    print(level[-1:-rank:-1])
    answer.append((level[-1:-rank:-1]))
    return answer[0].pop()


#levels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
levels = [i for i in range(1, 100)]
result = solution(levels)
print(result)
