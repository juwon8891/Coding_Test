word = input().lower()
new_list = list(set(word))
se_list = list()
for i in new_list:
    se_list.append(word.count(i))
if se_list.count(max(se_list)) > 1:
        print("?")
else:
    print(new_list[se_list.index(max(se_list))].upper())