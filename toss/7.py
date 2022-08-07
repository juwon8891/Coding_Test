from itertools import product


def solution(money, stocks):
    answer = 0
    before = []
    temp = []
    for stock in stocks:
        #temp.append(list(product(before, stock)))
        print(list(product(before, stock)))
        before = stock
    temp[1]
    return answer


# levels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
money = 30
stocks = [[1, 1], [3, 5], [3, 5], [4, 9]]
result = solution(money, stocks)
print(result)
