import re
n = input()
value = input()
numbers = re.findall(r'\d', value)
sum = 0
for i in numbers:
    sum += int(i)
print(sum)