def dfs(g, start):
    visited = [False] * len(g)
    
    def visit(v):
        print(f'visiting {v}')
        visited[v] = True
        for w in g[v]:
            if not visited[w]:
                visit(w)
    
    visit(start)

# adjacency list representation
graph = [
    [1, 2, 5, 6],
    [0],
    [0],
    [4, 5],
    [3, 5, 6],
    [0, 3, 4],
    [0, 4]
]

dfs(graph, 0)