def get_occurrence_count(my_list):
  new_list = {}
  for i in my_list:
    try: new_list[i] += 1
    except: new_list[i] = 1
  return(new_list)

def paperCuttings():
    dic = []
    cnt = 0
    textLength = int(input())
    starting = list()
    ending = list()
    new_list = list()
    normal = list()
    star_n = int(input())

    for i in range(1,textLength+1):
        normal.append(i)

    for i in range(star_n):
        starting.append(int(input()))
    end_n = int(input())
    for i in range(end_n):
        ending.append(int(input()))

    for i in range(0,star_n):
        new_list.append(normal[starting[i]:ending[i]])

    for i in range(1,textLength+1):
        new_list.append([i])

    items = sum(new_list, [])
    dic = get_occurrence_count(items)

    for key, value in dic.items():
        if value <= 2:
            cnt = cnt + 1
    print(new_list)
    print(cnt)
    print(dic)
#textLength = 10
#starting = [1,1,6,7]
#ending = [5, 3, 8, 10]
#starting = [3, 1, 2, 8, 8]
#ending = [5, 3, 7, 10, 10]
#8
#5
#[3,4,5,6,8]
#5
#[4,5,6,7,8]
paperCuttings()