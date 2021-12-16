import itertools
N,M = map(int,input().split())
N = [_ for _ in range(1,N+1)]
result = list(itertools.combinations_with_replacement(N,M))
for i in result:
    for j in i: 
        print(j, end=" ")
    print()