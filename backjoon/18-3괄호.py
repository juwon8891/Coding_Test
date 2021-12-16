import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    if len(a) % 2 == 0:
        for i in range(len(a)):
            if a[i] == a[-1]:
                print("NO")
                a.remove(i)
                a.pop()
print(a)