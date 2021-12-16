N,M =  map(int,input().split())
n_list = []
min_list = []
for _ in range(N):
    n_list.append(list(map(int,input().split())))
for i in n_list:
    min_list.append(min(i))
print(max(min_list))