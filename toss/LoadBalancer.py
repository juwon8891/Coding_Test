def solution(servers, sticky, requests):
    answers = [[] * servers for _ in range(servers)]
    cnt = 0
    point = 0
    for request in requests:
        check = cnt % servers
        check2 = point % servers
        if not sticky:
            answers[check].append(request)
        elif cnt == 0:
            answers.append(request)
            pass
        for answer in answers:
            if request in answer:
                answer.append(request)
                point = len(answers) - 1
        answers[point].append(request)
        cnt += 1
    return answers


servers = int(2)
sticky = True
# requests = [1,1,2,2]
requests = [1, 2, 2, 3, 4, 1]
result = solution(servers, sticky, requests)
print(result)
