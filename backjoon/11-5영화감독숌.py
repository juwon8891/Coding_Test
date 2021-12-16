N = int(input())
movie = 666 

while N: #브루탈포스 완전탐색
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)


""" 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다. """