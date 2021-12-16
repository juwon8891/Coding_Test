N = int(input())
def solutions(N):
    if N==1:
        return 1
    elif N==2:
        return 2
    elif N==3:
        return 4
    else:
        return solutions(N-1) + solutions(N-2) + solutions(N-3)

for i in range(N):
    n = int(input())
    print(solutions(n))