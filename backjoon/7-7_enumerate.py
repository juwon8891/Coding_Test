cls = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dialog = input()
sord = 0

for i in dialog:
    for idx, dial in enumerate(cls):
        if i in dial:
            sord += 3+idx
            break
print(sord)