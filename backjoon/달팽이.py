import math
a, b, v = map(int, input().split())
current = 0
day = (v-b) / (a-b)

# while True:
#     current = current + a
#     if current >= v:
#         break
#     current = current - b
#     day += 1

print(math.ceil(day))