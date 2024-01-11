'''
Write a function that takes a directed graph in adjacency list 
representation and two integer vertex ids v and w.
The function should return True if v and w are mutually reachable, i.e. 
there is some path from v to w and also from w to v.
'''

graph_adj_list = [
    [2, 5],
    [0],
    [0],
    [4], 
    [6], 
    [3], 
    [0]
]

def is_mutually_reachable(g_lst, v, w):
    is_path_from_v_to_w = is_path(g_lst, v, w)
    is_path_from_w_to_v = is_path(g_lst, w, v)

    if is_path_from_v_to_w and is_path_from_w_to_v:
        print(f'Vertices {v} and {w} are mutually reachable')
    elif is_path_from_v_to_w:
        print(f'There is a path from {v} to {w}, but not from {w} to {v}')
    elif is_path_from_w_to_v:
        print(f'There is a path from {w} to {v}, but not from {v} to {w}')
    else:
        print(f'There is no path between {v} and {w}')

def is_path(graph, start, goal):
    visited = [False] * len(graph)

    def visit(v):
        print(f'visiting {v}')
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                visit(w)
    visit(start)
    print()
    return visited[goal]

is_mutually_reachable(graph_adj_list, 5, 1)