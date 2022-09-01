MAX = 0
NOW = 0
for i in range(4): 
    N, M = map(int, input().split())
    NOW += M 
    NOW -= N
    if(MAX < NOW):
        MAX = NOW
print(MAX)