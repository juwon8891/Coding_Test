N = list(input().split())
list1 = list(N[0])
N[1] = int(N[1])
cnt = 0
print(ord("Z"))

for i in list1:
    list1[cnt] = ord(i) - 55
    cnt = cnt + 1

print(int("ZZZZZ",list1[0]))