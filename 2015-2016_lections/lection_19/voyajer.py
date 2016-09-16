def voyager(G, node, path = [], pathlen = 0, used = set()):
    global optimalpath, optimalpathlen
    if len(G) == len(used):
        if pathlen < optimalpathlen and node in G[path[-1]]:
            optimalpathlen = pathlen
            opltimalpath  = path
    else:
        for neighbour in G[node]:
            if neighbour not in used:
                voyager(G, neighbour, path + [neighbour],pathlen +
                        G[node][neighbour], used + {neighbour})
