def solution(today, terms, privacies):
    k_v = {}
    answer = []
    today_year = today[0:4]
    today_month = today[5:7]
    today_day = today[8:10]
    today_date = int(today_year + today_month + today_day)
    for i in terms:
        k_v[i[0]] = i[1:]
    for idx, privacie in enumerate(privacies):
        date, term = map(str, privacie.split())
        date_month = date[5:7]
        date_day = date[8:10]
        date_year = int(date[0:4])
        date_month = int(int(date_month) + int(k_v[term]))
        if date_month > 12:
            date_year += 1
            date_month -= 12
        if len(str(date_month)) == 1:
            date_month = "0" + str(date_month)
        current_date = (str(date_year) + str(date_month) + str(date_day))
        if int(today_date) >= int(current_date):
            answer.append(idx+1)
    return answer

today = "2022.05.19"
terms = ["A6", "B12", "C3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


result = solution(today, terms, privacies)
print(result)
