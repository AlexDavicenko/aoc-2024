from collections import defaultdict
DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()


ROWS = 103
COLS = 101

grid = [[[] for _ in range(COLS)] for _ in range(ROWS)]

for line in data.splitlines():
    pos, vel = line.split(" v=")

    px, py = pos.split("=")[1].split(",")

    vx, vy = vel.split(",")

    v = (int(vy),int(vx))
    grid[int(py)][int(px)].append(v)

ITERATIONS = 20000
seen = set()
for i in range(ITERATIONS):
    new_grid = [[[] for _ in range(COLS)] for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in grid[r][c]:
                nr, nc = (r+dr)%ROWS, (c+dc)%COLS
                new_grid[nr][nc].append((dr,dc))
    grid = new_grid

    pattern = []
    with open(f"output{DAY}.txt", "a") as out_file:
        out_file.write(f"Iteration {i}\n")
        for r in range(ROWS):
            for c in range(COLS):
                pattern.append(str(grid[r][c]))
                out_file.write(f"{'x' if len(grid[r][c]) >0 else '_'}")
            out_file.write("\n")
        jn_pattern = "".join(pattern)
        if jn_pattern in seen:
            break
        seen.add(jn_pattern)
        if "xxxxxxxx" in jn_pattern:
            print(i)
quads_1 = 0
quads_2 = 0
quads_3 = 0
quads_4 = 0

for r in range(ROWS):
    for c in range(COLS):

        if r < ROWS // 2 and c < COLS //2:
            quads_1 += len(grid[r][c])
        if r < ROWS // 2 and c > COLS //2:
            quads_2 += len(grid[r][c])
        if r > ROWS // 2 and c < COLS //2:
            quads_3 += len(grid[r][c])
        if r > ROWS // 2 and c > COLS //2:
            quads_4 += len(grid[r][c])
        
print(quads_1, quads_2, quads_3, quads_4)
print(quads_1 * quads_2 * quads_3 * quads_4)