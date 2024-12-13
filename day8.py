DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()
from collections import defaultdict

grid = [list(row) for row in data.splitlines()]
rows = len(grid)
cols = len(grid[0])

mp = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            mp[grid[r][c]].append((r,c))
res = set()
def in_bounds(node):
    return node[0] >= 0 and node[0] < rows and node[1] >= 0 and node[1] < cols

for points in mp.values():
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            #j->i
            print(points[i], points[j])
            diff = (points[i][0]-points[j][0],points[i][1]-points[j][1])
            antinodes = []
            k = 0
            while True:
                node = (points[i][0]+k*diff[0], points[i][1]+k*diff[1])
                if in_bounds(node):
                    antinodes.append(node)
                else:
                    break
                k += 1
            k = 0
            while True:
                node = (points[j][0]-k*diff[0], points[j][1]-k*diff[1])
                if in_bounds(node):
                    antinodes.append(node)
                else:
                    break
                k += 1
            for node in antinodes:
                grid[node[0]][node[1]] = "#"
                res.add(node)

for r in grid:
    print("".join(r))
print(len(res))