class Solution:
    def isPalindrome(x: int) -> bool:
        x_list = list(str(x))
        target = len(x_list) // 2
        cnt = 0
        for i in range(target):
            if x_list[i] == x_list[-1-i]:
                cnt = cnt + 1
        if cnt == target:
            return True
        else:
            return False
print(Solution.isPalindrome(10))