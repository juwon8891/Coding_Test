while 1:
    A = list(map(int, input().split()))
    max_n = max(A)
    A.remove(max_n)
    w = A[0] ** 2
    h = A[1] ** 2
    if sum(A) == 0:
        break
    if w+h  == max_n ** 2:
        print("right")
    else:
        print("wrong")