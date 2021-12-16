from collections import deque
N = int(input())
cnt = 0
for i in range(N):
    count, target = map(int, input().split())
    n_list = deque(list(map(int, input().split())))
    while n_list[target] < max(n_list):
        n_list.append(n_list.popleft()) 
    cnt = cnt + 1
    while n_list[target] == max(n_list):
        n_list.popleft()
        cnt = cnt + 1
    print(cnt)
    cnt = 0
#4 3 2 1