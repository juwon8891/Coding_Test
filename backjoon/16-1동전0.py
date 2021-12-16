N,K = map(int,input().split())
n_list = []
cnt = 0
for i in range(N):
    n_list.append(int(input()))
for i in range(N):
        quotient = K // n_list[N-i-1]
        remainder = K % n_list[N-i-1]
        if quotient:
            cnt = cnt + quotient 
            K = remainder
print(cnt)