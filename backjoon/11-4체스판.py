n, m = map(int, input().split())
chess_W = [[0] * m for _ in range(n)]
chess_B = [[0] * m for _ in range(n)]
arr = [list(input()) for _ in range(n)]
cnt = float('inf')
 
for i in range(n):
    for j in range(m):
        if not (i+j) % 2:
            chess_W[i][j] = 'W'
            chess_B[i][j] = 'B'
        else:
            chess_W[i][j] = 'B'
            chess_B[i][j] = 'W'
 
for i in range(n-7):
    for j in range(m-7):
        temp_W, temp_B = 0, 0
        for x in range(8):
            for y in range(8):
                if arr[i+x][j+y] != chess_W[i+x][j+y]:
                    temp_W += 1
                if arr[i+x][j+y] != chess_B[i+x][j+y]:
                    temp_B += 1
        cnt = min(cnt, temp_W)
        cnt = min(cnt, temp_B)
print(cnt)


""" w,h = map(int, input().split())
num = w * h
w_list = [] * h
cnt = 0
cnt2 = 0
k = 0
WB = ["W","B"]
WB2 = ["B","W"]
std_list = [[0 for j in range(h)] for i in range(w)]
std2_list = [[0 for j in range(h)] for i in range(w)]
for i in range(w):
    w_list.append(list(input()))

for i in range(w):
    std_list[i][0] = WB[i%2]
    std2_list[i][0] = WB2[k%2]
    for j in range(1,h):
        std_list[i][j] = WB[1] if std_list[i][j-1] == WB[0] else WB[0]
        std2_list[i][j] = WB[1] if std_list[i][j-1] == WB[1] else WB[0]
    k = k + 1
for i in range(w):
    for j in range(h):
        if w_list[i][j] != std_list[i][j]:
            cnt = cnt + 1
        if w_list[i][j] != std2_list[i][j]:
            cnt2 = cnt2 + 1
result = min(cnt, cnt2)
print(result) """