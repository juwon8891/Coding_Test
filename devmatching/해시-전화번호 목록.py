# def solution(phone_book):
#     n = len(phone_book)
#     phone_book.sort()
#     answer = True
#     for i in range(n-1):
#         if len(phone_book[i]) < len(phone_book[i+1]):
#             if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
#                 answer == False
#                 break
#     return answer
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    zip_phone = list(zip(phone_book, phone_book[1:]))
    for p1,p2 in zip_phone:
        if p2.startswith(p1):
            return False
    return True

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))