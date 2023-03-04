from collections import deque

def minimumTreePath(n, edges, visitNodes):
    # Create an adjacency list to represent the tree
    adj_list = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Perform a breadth-first search from node 1 to each node in visitNodes
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

    # If we get here, we couldn't find a path from 1 to any node in visitNodes
    return -1





# n = 5
# edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
# visitNodes = [2, 4]
n = 3
edges = [[1, 2], [1, 3]]
visitNodes = [2]
print(minimumTreePath(n, edges, visitNodes))  # 6