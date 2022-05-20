def solution(a, v):
    def dfs(pos, cur):
        if pos == len(a):
            return (cur == 0)
        return dfs(pos + 1, cur + a[pos]) + dfs(pos + 1, cur - a[pos])
    return dfs(0, v)
a = [1, 1, 1, 1, 1]
v = 3
print(solution(a,v))