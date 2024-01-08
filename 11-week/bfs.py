from collections import deque
from read_graph import read_graph

# breadth first search over a graph with integer ids
# def bfs(graph, start):
#     visited = [False] * len(graph)
#     visited[start] = True

#     q = deque()
#     q.append(start)

#     while len(q) > 0:
#         v = q.popleft()
#         print(f'visiting {v}')

#         for w in graph[v]:
#             if not visited[w]:
#                 visited[w] = True
#                 q.append(w)

# graph = [
#     [1, 2, 3],
#     [0, 4],
#     [0, 5],
#     [0, 6],
#     [1],
#     [2],
#     [3]
# ]
# bfs(graph, 3)

# def bfs(graph, start):
#     visited = { start }

#     q = deque()
#     q.append((start, 0))

#     while len(q) > 0:
#         v, dist = q.popleft()
#         print('  ' * dist + v)

#         for w in graph[v]:
#             if w not in visited:
#                 q.append((w, dist+1))
#                 visited.add(w)

# europe = read_graph()
# bfs(europe, 'ireland')


def bfs(graph, start, goal):
    visited = { start }
    pred = { }

    q = deque()
    q.append(start)
    pred[start] = None

    while len(q) > 0:
        v = q.popleft()
        if v == goal:
            path = []
            while True:
                path.append(v)
                if pred[v] == None:
                    break
                v = pred[v]
            path.reverse()
            return path

        for w in graph[v]:
            if w not in visited:
                q.append(w)
                visited.add(w)
                pred[w] = v

europe = read_graph()
path = bfs(europe, "germany", "portugal")
print(path)