n = int(input())
body = list()
temp_num, max_num = 0, 0
for i in range(n):
    body.append(list(map(int, input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if (body[i][0] < body[j][0]) and (body[i][1] < body[j][1]):
                rank +=1
    print(rank,end=' ') 