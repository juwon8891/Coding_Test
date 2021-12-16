N = int(input())
real = list(map(int, input().split()))

max_num = max(real)
min_num = min(real)

print(max_num * min_num)