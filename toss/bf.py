def solution(nums, target):
    temp = []
    for num in nums:
        for i in range(len(num) - 1):
            for j in range(i, len(num)):
                if num[i] + num[j] == target:
                    if [num[i], num[j]] not in temp:
                        temp.append([num[i], num[j]])
    return temp


# levels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
nums = [[1, 1], [3, 5], [3, 5], [4, 9]]
lists = sum(nums, [])
num = [2,7,11,15,15]
result = solution(nums, target)
print(result)
