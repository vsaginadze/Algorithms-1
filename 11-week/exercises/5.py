from collections import deque

graph = [
    [1, 2, 5],
    [0],
    [0],
    [4], 
    [6], 
    [3, 4], 
    [0]
]

def shortest_path(graph, start, goal):
    visited = [False] * len(graph)
    visited[start] = True

    q = deque()
    q.append((start, 0))

    while len(q) > 0:
        v, d = q.popleft()
        print(f'visiting {v}')
        
        if v == goal:
            print(f'\ndistance -> {d}')
            break

        for w in graph[v]:
            if w not in visited:
                q.append((w, d+1))
                visited[w] = True