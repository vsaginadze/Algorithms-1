graph = [
    [1, 2, 5, 6],    # neighbors of 0
    [0],             # neighbors of 1
    [0],             # …
    [4, 5],
    [3, 5, 6],
    [0, 3, 4],
    [0, 4]
]

def dfs(graph, start):
    visited = [False] * len(graph)

    def visit(v):
        print(f'visiting {v}')
        visited[v] = True
        
        for w in graph[v]:
            if not visited[w]:
                visit(w)

    visit(start)

dfs(graph, 0)