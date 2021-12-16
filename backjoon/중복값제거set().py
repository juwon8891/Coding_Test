import sys, re
from typing import Set
def inputs():
    return sys.stdin.readline().rstrip()

a=list()
b = [0 for i in range(10)]
for i in range(10):
  a.append(int(inputs()))

for i in range(10):
  b[i] = a[i] % 42
quiz = len(set(b)) 
print(quiz)