from collections import deque
import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    cmd = list(input())
    length = int(input())
    n_list = input().replace("[","")
    n_list = n_list.replace("]","")
    n_list = deque(n_list.split(","))
    D_len = cmd.count("D")
    if D_len >= len(n_list):
        print("error")
        continue
    for i in cmd:
        if i == "R":
            n_list.reverse()
        elif i == "D":
            n_list.popleft()
    print(list(map(int,n_list)))