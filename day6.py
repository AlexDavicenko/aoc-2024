with open("input6.txt", "r") as f:
    data = f.read()
grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])
for row in range(rows):
    grid[row] = list(grid[row])
start_r, start_c = 0, 0 
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            start_r, start_c = r,c 


res = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "#": continue
        grid[i][j] = "#"

        positions = set()
        dr, dc = -1, 0
        idx = 0
        directions = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1),
        ]
        r, c = start_r, start_c
        while True:
            if (r,c,idx) in positions:
                res += 1
                break
            positions.add((r,c, idx))
            off_map = False
            while True:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == "#":
                        idx = (idx+1)%4
                        dr, dc = directions[idx]
                    else:
                        r += dr
                        c += dc
                        break 
                else:
                    off_map = True
                    break
            if off_map:
                break
        grid[i][j] = "."

print(len(positions))
print(res)



"""

with open("input6.txt", "r") as f:
    data = f.read()
grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])

start_r, start_c = 0, 0 
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            start_r, start_c = r,c 
print(start_r, start_c)
print(grid)


positions = set()
dr, dc = -1, 0
idx = 0
directions = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]
r, c = start_r, start_c
while True:
    positions.add((r,c))
    off_map = False
    while True:
        nr, nc = r + dr, c + dc

        if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
            if grid[nr][nc] == "#":
                idx = (idx+1)%4
                dr, dc = directions[idx]
            else:
                r += dr
                c += dc
                break 
        else:
            off_map = True
            break
    if off_map:
        break
print(len(positions))

"""