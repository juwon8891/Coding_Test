N = []
for i in range(8):
    N.append(list(map(str,input())))
cnt = 0
bulse = False
for i in N:
    bulse = not bulse
    for j in range(8):
        if i[j] == "F" and bulse == True:
            cnt = cnt + 1 
        bulse = not bulse
print(cnt)