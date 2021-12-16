import math
t = int(input())
s = []
a = []
gcd = 0
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)
a.append(gcd)
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')
#아래는 메모리 초과 코드 처음 짠 것
""" import sys
def inputs():
    return sys.stdin.readline().rstrip()
N = int(inputs())
n_list = []
nmg = []
for i in range(N):
    n_list.append(int(inputs()))
n_list.sort()
for i in n_list:
    nmg_list = []
    for j in range(1,min(n_list)+2):
        nmg_list.append(i%j)
    nmg.append(nmg_list)
result = nmg[0]
for i in range(1,len(nmg)):
    result = list(set(nmg[i]) & set(result))
for j in range(2,min(n_list)):
    if n_list[0] % j in result:
        print(j, end=" ")
        result.remove(n_list[0] % j) """

