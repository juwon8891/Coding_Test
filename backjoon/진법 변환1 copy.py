N, B = input().split()

N = N[::-1]
B = int(B)

table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = 0

for i in range(len(N)):
    res += table.index(N[i]) * (B ** i)

print(res)