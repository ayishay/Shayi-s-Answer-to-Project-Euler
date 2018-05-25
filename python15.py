m = 5
n = 5

grid = {(m, n):1}

for i in reversed(range(m+1)):
    for j in reversed(range(n+1)):
        if i==m and j==n:
            continue
        grid[(i,j)] = grid.get((i+1, j),0) + grid.get((i, j+1),0)

print(grid)