adjacent_list = [
    [1, 2, 5, 6],
    [0],
    [0],
    [4, 5], 
    [3, 5, 6], 
    [0, 3, 4], 
    [0, 4]
]

def graph_list_to_matrix(g_list):
    g_matrix = []
    for adjacents in g_list:
        row = [False] * len(g_list)
        for vertex in adjacents:
            row[vertex] = True
        g_matrix.append(row)
    return g_matrix

adjacent_matrix = graph_list_to_matrix(adjacent_list)
print(adjacent_matrix)