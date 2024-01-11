'''
Write a function that takes an undirected graph in adjacency matrix representation, 
with integer vertex ids. The function should return True if the graph is connected, i.e. 
there is some path between every pair of vertices.
'''
graph = [
    [False, False,  True,  False, False, True,  True],
    [False,  False, False, False, False, False, False],
    [True,  False, False, False, False, False, False],
    [False, False, False, False, True,  True,  False],
    [False, False, False, True,  False, True,  True],
    [True,  False, False, True,  True,  False, False],
    [True,  False, False, False, True,  False, False]
]

def is_connected(graph):
    if not find_unvisited_node(graph, 0):
        print("Connected Graph")
    else:
        print("Graph is NOT connected")

def find_unvisited_node(graph, start):
    visited = [False] * len(graph)

    def visit(v):
        print(f'visiting {v}')
        visited[v] = True
        for w_idx in range(len(graph[v])):
            if graph[v][w_idx]:
                if not visited[w_idx]:
                    visit(w_idx)

    visit(start)
    print("--------")
    return False in visited

is_connected(graph)