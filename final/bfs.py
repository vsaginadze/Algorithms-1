graph = [
    [1, 2, 5, 6],    # neighbors of 0
    [0],             # neighbors of 1
    [0],             # …
    [4, 5],
    [3, 5, 6],
    [0, 3, 4],
    [0, 4]
]

from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque()

    q.append((start, 0))
    visited.add(start)

    while len(q) > 0:
        v, dist = q.popleft()
        print('  ' * dist + str(v))

        for w in graph[v]:
            if w not in visited:
                q.append((w, dist + 1))
                visited.add(w)

bfs(graph, 0)