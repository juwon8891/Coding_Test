import sys, re
def inputs():
    return sys.stdin.readline().rstrip()

a, b, c = inputs(), inputs(), inputs()
d = int(a) * int(b) * int(c)
e = [0 for i in range(10)] #리스트 0으로 초기화 e[10]

numbers = re.findall(r'\d', str(d)) # 숫자 리스트로 변환
# ######
# for i in range(len(numbers)):
#   if int(numbers[i]) == 0:
#     e[0] += 1
#   if int(numbers[i]) == 1:
#     e[1] += 1
#   if int(numbers[i]) == 2:
#     e[2] += 1
#   if int(numbers[i]) == 3:
#     e[3] += 1
#   if int(numbers[i]) == 4:
#     e[4] += 1
#   if int(numbers[i]) == 5:
#     e[5] += 1
#   if int(numbers[i]) == 6:
#     e[6] += 1
#   if int(numbers[i]) == 7:
#     e[7] += 1
#   if int(numbers[i]) == 8:
#     e[8] += 1
#   if int(numbers[i]) == 9:
#     e[9] += 1
# ######

for i in range(10):
  f = str(d).count(str(i))
  e[i] = f
  print(e)