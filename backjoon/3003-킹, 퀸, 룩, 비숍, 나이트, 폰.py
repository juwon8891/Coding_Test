correct = [1, 1, 2, 2, 2, 8]
answer = []
N = list(map(int, input().split()))

for i in range(len(correct)):
    print(correct[i] - N[i], end=" ")