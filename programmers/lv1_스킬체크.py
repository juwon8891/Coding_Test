from collections import Counter
def solution(N, stages):
    answer = []
    n_list = []
    n2_list = []
    fail_per = []
    j = 0
    cnt = Counter(stages)
    for i in range(1,N+1):
        n_list.append(cnt[i])
    #print(n_list.index(max(n_list)))
    for i in range(N):
        fail_per.append(round(n_list[i] / (len(stages) - j),2))
        j = n_list[i]
    for i in range(N):
        n2_list.append(fail_per.index(max(fail_per)))
        fail_per.remove(fail_per.index(max(fail_per)))
    for i in range(N):
        print(n2_list[i])
  
        #n_list.remove(n_list[i])
    print(fail_per)
    print(n_list)
    return answer       
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)