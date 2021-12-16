import re
#numbers = re.findall(r'\d', a)
sum = 1
while(1):
    a = list(map(int, input().split()))
    sum = a[0] + a[1]
    if sum == 0:
        break
    print(sum)
    