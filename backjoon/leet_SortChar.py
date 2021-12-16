class Solution:
    def frequencySort(s: str) -> str:
        s_list = list(s)
        n_list = {}
        for i in s_list:
            n_list[i] = s_list.count(i)
        return n_list
print(Solution.frequencySort("tree"))