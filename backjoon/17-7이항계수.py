def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def binofact(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)
a, b = map(int, input().split())
print(binofact(a,b))