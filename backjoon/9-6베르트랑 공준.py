M, N = map(int, input().split())
list = [_ for _ in range(M,N+1)]
n = []
for i in list:
    if i <= 1:
        list.remove(i)
    if i == 2:
        n.append(i)
    if i % 2 == 0 or i % 3 ==0 or i % 5 == 0:
        list.remove(i)
    if i == 3:
        n.append(i)
    if i % 3 == 0:
        list.remove(i)
    if i == 5:
        n.append(i)
    if i % 5 == 0:
        list.remove(i)
    if i == 7:
        n.append(i)
    if i % 7 == 0:
        list.remove(i)

print(list)
print(n)