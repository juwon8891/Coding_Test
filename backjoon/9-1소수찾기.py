N = int(input())
M = list(map(int,input().split()))
result = 0
for i in M:
    cnt = 0
    for j in range(1,max(M)+1):
        if i % j == 0:
            cnt = cnt + 1
    if cnt == 2:
        result += 1
print(result)