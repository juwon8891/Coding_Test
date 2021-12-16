import sys, re
n = int(input())  # 과목 수
for _ in range(n):
    cnt = 0
    test_list = list(map(int, input().split()))
    avg = (sum(test_list)-test_list[0])/test_list[0] #sum(arr)-arr[0] == sum(arr[1:])
    for score in test_list[1:]:
        if avg < score:
            cnt = cnt+1
    total = cnt / test_list[0] * 100
    print(f"{total:.3f}%")