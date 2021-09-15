
# Given a directed graph,
# find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph.
# Here reachable mean that there is a path from vertex i to j.
# The reach-ability matrix is called transitive closure of a graph.


def tclosure(G):
    n = len(G)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = G[i][j] or (G[i][t] and G[t][j])
    return G


G = [[False, True, False],
    [False, False, True],
    [False, False, False]]
print(tclosure(G))
# wypisze
    # [[False, True , True],
    # [False, False, True],
    # [False, False, False]]

#moj przyklad
print()
G2 = [
    [False, True, False, False, False],
    [False, False, False, False, True],
    [True, True, False, False, False],
    [False, False, True, False, True],
    [False, False, False, False, False]
]
print(tclosure(G2))