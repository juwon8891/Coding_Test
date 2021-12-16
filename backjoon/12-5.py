import re

second = input()
numbers = re.findall(r'\d', second)
a = ""
numbers.sort()
numbers.reverse()
for i in numbers:
    a = a + i
print(a)