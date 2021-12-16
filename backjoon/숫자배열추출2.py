input_data = int(input())
N = input_data
count = 0
num = N

while True:
  num_1 = num // 10 #목
  num_2 = num % 10 # 나머지
  num_3 = (num_1 + num_2) % 10 #몫+나머지의 나머지
  num = (num_2 * 10) + num_3
  count += 1

  if num == N:
    print(count)
    break