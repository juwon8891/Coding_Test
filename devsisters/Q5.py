from collections import deque

def minimumTreePath(n, edges, visitNodes):
    # Convert edge list to adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # Find the shortest path that connects the nodes in visitNodes
    pq = deque(visitNodes)
    dist = [-1] * n
    dist[visitNodes[0]-1] = 0
    while pq:
        u = pq.popleft()
        for v in adj[u-1]:
            if dist[v] == -1:
                dist[v] = dist[u-1] + 1
                pq.append(v+1)
    path = [dist[u-1] for u in visitNodes]

    # Compute the distances from the nodes to their nearest ancestor in the path
    dist_ancestors = [-1] * n
    for u in visitNodes:
        v = u
        while v != -1 and dist_ancestors[v-1] == -1:
            dist_ancestors[v-1] = dist[u-1]
            v = parent[v-1]

    # Perform DFS to construct the tree and compute the distances
    parent = [-1] * n
    depth = [-1] * n
    stack = [0]
    depth[0] = 0
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                stack.append(v)
    ans = sum(path)
    for u, v in edges:
        if (u not in visitNodes) != (v not in visitNodes):
            if u in visitNodes:
                ans += depth[u-1] - dist_ancestors[u-1] + 1
            else:
                ans += depth[v-1] - dist_ancestors[v-1] + 1
    return ans





# n = 5
# edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
# visitNodes = [2, 4]
n = 3
edges = [[1, 2], [1, 3]]
visitNodes = [2]
print(minimumTreePath(n, edges, visitNodes))  # 6