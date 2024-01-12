from collections import deque

tree = {
    0: [3, 4],
    3: [5, 6],
    5: [],
    6: [],
    4: [8, 9],
    8: [12],
    9: [],
    12: []
}


def on_the_path(tree, start, goal, end):
    visited = {start}
    unique_path = []

    def visit(v):
        print(f'visiting {v}')
        
        visited.add(v)
        unique_path.append(v)

        if v == end:
            return goal in unique_path
        
        for w in tree[v]:
            if w not in visited:
                if visit(w):
                    return True
        unique_path.pop()
        

    return True if visit(start) else False
    

print(on_the_path(tree, 0, 12, 9))

