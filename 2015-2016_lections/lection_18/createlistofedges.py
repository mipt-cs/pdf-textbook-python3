edges = [] 
for vertex in G:
    for neighbour in G(vertex):
        edges.append(vertex, neighbour)
