from collections import deque
n = 5
edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
visitNodes = [2, 4]
def minimumTreePath(n, edges, visitNodes):
    adj_list = {i: [] for i in range(1, n+1)}
    for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
    queue = deque([(1, 0)])
    visited = set()
    visited.add(1)
    while queue:
            node, dist = queue.popleft()
            if node in visitNodes:
                return dist
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist+1))
print(minimumTreePath(n, edges, visitNodes))