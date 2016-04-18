N = int(input())
G = {}
k = int(input())
for i in range(k):
    a, b = [int for x in input().split()]
    if a not in G:
        G[a] = {b}
    else:
        G[a].insert(b)
