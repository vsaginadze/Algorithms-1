# def dfs(g, start):
#     visited = [False] * len(g)

#     def visit(v):
#         print(f'visiting {v}')
#         visited[v] = True
#         for w in g[v]:
#             if not visited[w]:
#                 visit(w)
    
#     visit(start)


def dfs(g, start):
    visited = [False] * len(g)

    def visit(v):
        print(f'visiting {v}')
        visited[v] = True
        for w in g[v]:
            if not visited[w]:
                visit(w)
    visit(start)


# # adjacency list representation
# graph = [
#     [1, 2, 5, 6],
#     [0],
#     [0],
#     [4, 5],
#     [3, 5, 6],
#     [0, 3, 4],
#     [0, 4]
# ]

# dfs(graph, 0)

# from read_graph import read_graph

# europe = read_graph()
# print(europe)

# def dfs(g, start):
#     visited = set()

#     def visit(v, depth):
#         print('  ' * depth + v)
#         visited.add(v)
#         for w in g[v]:
#             if w not in visited:
#                 visit(w, depth + 1)
    
#     visit(start, 0)

# europe = read_graph()
# dfs(europe, 'ireland')