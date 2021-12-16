n = int(input())
empy = list()
for i in range(n):
    empy.append(int(input()))
empy.sort()
empy.reverse()
for i in empy:
    print(i)
