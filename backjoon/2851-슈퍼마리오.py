a_list = [int(input()) for _ in range(10)]
check = 0
before = 0
if sum(a_list) <= 100:
    print(sum(a_list))
for idx, i in enumerate(a_list):
    check += i
    if check > 100:
        if abs(100 - before) < abs(100 - check):
            print(before)
            break
        else:
            print(check)
            break
    before = check