graph = [
    [False, True,  True,  False, False, True,  True],
    [True,  False, False, False, False, False, False],
    [True,  False, False, False, False, False, False],
    [False, False, False, False, True,  True,  False],
    [False, False, False, True,  False, True,  True],
    [True,  False, False, True,  True,  False, False],
    [True,  False, False, False, True,  False, False]
]

def graph_matrix_to_list(graph_matrix):
    graph_list = []
    for v_adjacents in graph_matrix:
        l = []
        for idx in range(len(v_adjacents)):
            if v_adjacents[idx]:
                l.append(idx)
        graph_list.append(l)

    return graph_list

graph_list = graph_matrix_to_list(graph)
print(graph_list)