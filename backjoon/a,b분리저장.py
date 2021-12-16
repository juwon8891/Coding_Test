import re
#numbers = re.findall(r'\d', a)
while 1:
    try:
        a,b = map(int, input().split())
        sum = a+b
        print(sum)
    except:
        break
    
    