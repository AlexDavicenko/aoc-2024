DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()

grid = [list(map(int, list(row))) for row in data.splitlines()]
rows = len(grid)
cols = len(grid[0])

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            stack = [(r, c)]
            visited = set([(r,c)])
            while stack:
                row, col = stack.pop()
                if grid[row][col] == 9:
                    res += 1
                for dr, dc in [
                    (1,0),
                    (-1,0),
                    (0,1),
                    (0,-1),
                ]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr and nr < rows and 0 <= nc and nc < cols and (nr,nc) not in visited:
                        if grid[nr][nc] == grid[row][col] + 1:
                            visited.add((nr,nc))
                            stack.append((nr,nc))
print(res)