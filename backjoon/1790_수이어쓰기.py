N, M = map(int,(input().split()))
answer = ""
for i in range(1,M+1):
    answer += str(i)
    if len(answer) == N:
        break
print(list(answer)[N+2])