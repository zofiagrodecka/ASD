#dla listy sasiedztwa:

def DFSVisit(G, visited, colours, u):
    cycle = False
    visited[u] = True
    colours[u] = "gray"
    for v in G[u]:
        if colours[v] == "white":
            cycle = cycle or DFSVisit(G, visited, colours, v)
        elif colours[v] == "gray":
            cycle = True
    colours[u] = "black"
    return cycle

def detect_cycle(G):
    n = len(G)
    visited = [False] * len(G)
    colours = ["white"]*len(G)
    cycle = False
    for v in range(n):
        if colours[v] == "white":
            cycle = cycle or DFSVisit(G, visited, colours, v)
    return cycle, colours


graf = [[1,2], [], [], [], [3,2]]
print(detect_cycle(graf))
G = [[1,2],[2],[4,3],[1],[5],[3],[7,2],[]]
print(detect_cycle(G))
