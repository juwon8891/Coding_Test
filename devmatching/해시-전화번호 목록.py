import re

def solution(registered_list, new_id):
    answer = new_id
    strings = re.findall('[a-z]', answer)
    N = "1"
    N1 = "11"
    numbers = re.findall('\d', answer)
    for _ in registered_list:
        if answer not in registered_list:
            break
        elif answer in registered_list:
            if not numbers:
                N = 0
            if len(N1) != len(str(N)):
                numbers = re.findall('\d', answer)
            elif numbers:
                numbers = re.findall('\d', answer)
                N = ''.join(s for s in numbers)
            S = ''.join(s for s in strings)
            N1 = str(int(N) + 1)
            new_id1 = S + N1
            answer = new_id1
    return answer

registered_list = ["cow","cow1","cow2","cow3","cow4", "cow10"]
new_id = "cow"
print(solution(registered_list, new_id))