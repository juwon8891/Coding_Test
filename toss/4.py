def solution(invitationPairs):
    answer = 0
    for i in range(len(invitationPairs)):
        for j in range(i+1, len(invitationPairs)):
            if invitationPairs[i][0] == invitationPairs[j][0] or invitationPairs[i][1] == invitationPairs[j][1]:
                answer += 1

    return answer


# levels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
invitationPairs = [
    [1, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [5, 6],
    [5, 7],
    [5, 8],
    [6, 8],
    [2, 9],
]
result = solution(invitationPairs)
check = list(zip(*invitationPairs))[0]
print(check)
a = {}
a.copy(1,2)
print(a)
for i in check:
    a.get(i, check.count(i))
print(check.count())
print(a)
