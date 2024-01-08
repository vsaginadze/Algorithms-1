path = "/Users/vsaginadze/Desktop/Comp-Sci/Algorithms-1/11-week/europe.txt"
def read_graph():
    g = {}

    def add(v, w):
        if v not in g:
            g[v] = []
        g[v].append(w)
    
    with open(path) as f:
        for line in f:
            source, dest = line.split(":")
            if source not in g:
                g[source] = []
            for c in dest.split():
                add(source, c)
                add(c, source)
    return g