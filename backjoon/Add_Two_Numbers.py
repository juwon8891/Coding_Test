class Solution:
    def twoSum(l1, l2):
        a = ""
        b = ""
        one = l1[::-1]
        for i in one:
            a += str(i)
        two = l2[::-1]
        for i in two:
            b += str(i)
        result = int(a) + int(b)
        c = reversed(list(str(result)))
        return list(c)
l1 = [2,4,3]
l2 = [5,6,4]
print(Solution.twoSum(l1, l2))