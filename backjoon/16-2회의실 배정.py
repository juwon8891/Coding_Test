import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
n_list = []
result_list = []
cnt = 0
for i in range(N):
    start, end = map(int, input().split())
    n_list.append((start,end))

n_list.sort(key = lambda x: (x[1], x[0]))
result_list.append(n_list[0])
for i in range(1,len(n_list)):
    if result_list[cnt][1] <= n_list[i][0]:
            result_list.append(n_list[i])
            cnt = cnt + 1
print(cnt+1)