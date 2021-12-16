N = int(input())
a = []
for i in range(N):
    a.append(input().lower()) #ord
a = list(set(a))
sort = []
for i in a:
    sort.append((len(i), i))
result = sorted(sort)
for len,word in result:
    print(word)