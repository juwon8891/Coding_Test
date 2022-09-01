from itertools import combinations as cb
N, M = map(int, input().split())
W = []
V = []
checkNumber = 0
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for a, b in cb(V, 2):
    checkNumber = a + b
    if checkNumber > W:
        pass
    print(checkNumber)


print(N,M)
print(W,V)