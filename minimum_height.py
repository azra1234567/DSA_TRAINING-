from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()

        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n

        while remaining > 2:
            leaves = len(q)
            remaining -= leaves

            for _ in range(leaves):
                node = q.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)