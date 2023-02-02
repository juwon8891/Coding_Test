from itertools import combinations, permutations

must = 2
for i, j in permutations([1,7,14,10], 2):
    if i != must and j != must:
        continue
    answer = [i,j]
    print(answer, end=" ")