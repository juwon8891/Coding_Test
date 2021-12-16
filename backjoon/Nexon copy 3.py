import sys
n,x = map(int, sys.stdin.readline().rstrip().split())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
for i in seq:
    if i < x:
        print(i,end=" ")