def solution(s):
    answer = []
    a = int(0)
    b = int(3)
    maginNumber = ["111", "222", "333", "444", "555", "666", "777", "888", "999"]
    while a != len(s):
        if s[a:b] in maginNumber:
            answer.append(int(s[a:b]))
        a += 1
        b += 1
    if answer == []:
        return -1
    else: return sorted(answer)[-1]

sticky = True
# requests = [1,1,2,2]
requests = [1, 2, 2, 3, 4, 1]
s = "12223"
s2 = "111999333"
result = solution(s2)
print(result)
