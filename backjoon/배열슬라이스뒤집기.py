A, B = map(str, input().split())
A1 = ''.join(reversed(A))
B1 = ''.join(reversed(B))
if A1 > B1: print(A1)
else: print(B1)

A, B = map(str, input().split())
A1 = A[::-1]
B1 = B[::-1]
if A1 > B1: print(A1)
else: print(B1)