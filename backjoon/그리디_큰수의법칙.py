N,M,K= map(int,input().split())
#N=배열크기, M=더하는 횟수, K=연속해서 덧셈 K번 초과불가
number = sorted(list(map(int,input().split())))
max_number = number[-1]
next_number = number[-2]
result = 0
if max_number == next_number:
    result = max_number * M
else:
    for i in range(1,M+1):
        if i % (K+1) == 0:
            result = result + next_number
        else:
            result = result + max_number
print(result)