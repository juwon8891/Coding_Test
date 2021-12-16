N = int(input())
for i in range(N):
    A,B = map(int, input().split())
    LCM = A*B
    while(1):
        temp = A % B
        if temp == 0:   
            break
        else:
            A = B
            B = temp
    GCD = B
    LCM = int(LCM / GCD)
    print(LCM)