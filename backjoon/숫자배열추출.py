#a = list(map(int, input().split()))
import re
first = int(input())
second = input()
numbers = re.findall(r'\d', second)
print(first*int(numbers[2]))
print(first*int(numbers[1]))
print(first*int(numbers[0]))
print(int(first)*int(second))