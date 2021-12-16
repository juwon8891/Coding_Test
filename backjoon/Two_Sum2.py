class Solution:
    def twoSum(nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
num = [2,7,11,15]
targets = 9
print(Solution.twoSum(num, targets))