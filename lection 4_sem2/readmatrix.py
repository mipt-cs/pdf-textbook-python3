k = int(input())
M = [[0]*N for i in range(N)]
for i in range(k):
     a, b = input().split()
     a, b = int(a), int(b)
     M[a][b] = 1
     M[b][a] = 1
