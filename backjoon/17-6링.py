def LCM(A,B):
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
    return GCD

N = int(input())
s = list(map(int, input().split()))
for i in range(1,N):
    m = s[0] // LCM(s[0], s[i])
    nmg = s[i] // LCM(s[0], s[i])
    print("{}/{}".format(m, nmg))