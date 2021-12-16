class Solution(object):
    def isPalindrome(x):
       return str(x) == str(x)[::-1]
print(Solution.isPalindrome(1211))