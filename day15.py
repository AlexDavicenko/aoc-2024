DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()

input_grid, directions = data.split("\n\n")
input_grid = list(map(list, input_grid.splitlines()))

mp = {
    "^": (-1,0),
    "v": (1,0),
    ">": (0,1),
    "<": (0,-1),
}

rows = len(input_grid)
cols = len(input_grid[0])
def find_robot(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                return row, col

def part1(grid, directions):
    rows = len(grid)
    cols = len(grid[0])
    r, c = find_robot(grid)

    for dir in directions:
        if dir == "\n": continue
        dr, dc = mp[dir]
        nr, nc = r + dr, c + dc

        #print(r, c, dir)
        if grid[nr][nc] == "#":
            continue
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            r, c = nr, nc
        if grid[nr][nc] == "O":
            i = 1
            while grid[r+dr*i][c+dc*i] == "O":
                i += 1
            if grid[r+dr*i][c+dc*i] == ".":
                grid[nr][nc], grid[r+dr*i][c+dc*i] = grid[r+dr*i][c+dc*i], grid[nr][nc]
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                r, c = nr, nc
        #for row in grid:
        #    print("".join(row))

    res = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "O":
                res += 100 * row + col
    print(res)

expanded_grid = [[] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if input_grid[row][col] == "O":
            expanded_grid[row].append("[")
            expanded_grid[row].append("]")
        elif input_grid[row][col] == "@":
            expanded_grid[row].append("@")
            expanded_grid[row].append(".")
        else:
            expanded_grid[row].append(input_grid[row][col])
            expanded_grid[row].append(input_grid[row][col])


def part2(grid, directions):
    
    rows = len(grid)
    cols = len(grid[0])
    r, c = find_robot(grid)

    for idx,dir in enumerate(directions):
        print(dir)
        if idx == 8862:
            for row in grid:
                print("".join(row))
        if dir == "\n": continue
        dr, dc = mp[dir]

        nr, nc = r + dr, c + dc

        #print(r, c, dir, grid[nr][nc])
        if grid[nr][nc] == "#":
            continue
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            r, c = nr, nc
        if grid[nr][nc] == "[" or grid[nr][nc] == "]":
            
            if dr == 0:
                i = 1
                while grid[r+dr*i][c+dc*i] == "[" or grid[r+dr*i][c+dc*i] == "]":
                    i += 1
                if grid[r+dr*i][c+dc*i] == ".":
                    while i != 0:
                        grid[r+dr*i][c+dc*i], grid[r+dr*(i-1)][c+dc*(i-1)] = grid[r+dr*(i-1)][c+dc*(i-1)], grid[r+dr*i][c+dc*i]
                        i += -1

                    r, c = nr, nc
            else:
                stack = []
                if grid[nr][nc] == "[":
                    stack.append((nr,nc,nr,nc+1))
                else:
                    stack.append((nr,nc-1,nr,nc))
                possible = True
                to_move = []
                visited = set()
                while stack:
                    lr,lc,rr,rc = stack.pop(0)
                    to_move.append((lr,lc,rr,rc))
                    nlr,nlc,nrr,nrc = lr+dr, lc+dc, rr+dr, rc+dc
                    if grid[nlr][nlc] == "#" or grid[nrr][nrc] == "#":
                        possible = False
                        break
                    for dfs_r, dfs_c in [(nlr,nlc), (nrr,nrc)]:
                        if grid[dfs_r][dfs_c] == "]":
                            box = (dfs_r,dfs_c-1,dfs_r,dfs_c)
                            if box not in visited:
                                visited.add(box)
                                stack.append(box)
                        elif grid[dfs_r][dfs_c] == "[":
                            box = (dfs_r,dfs_c,dfs_r,dfs_c+1)
                            if box not in visited:
                                visited.add(box)
                                stack.append(box)

                if possible:
                    print("UP")
                    to_move.reverse()
                    for lr,lc,rr,rc in to_move:
                        grid[lr][lc], grid[lr+dr][lc] = grid[lr+dr][lc], grid[lr][lc]
                        grid[rr][rc], grid[rr+dr][rc] = grid[rr+dr][rc], grid[rr][rc]
                    grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                    r, c = nr, nc
        #fail if [[ or ]] detected
        br = False
        for r_ in range(rows):
            for c_ in range(cols-1):
                if (grid[r_][c_] == "[" and grid[r_][c_+1] == "[") or (grid[r_][c_] == "]" and grid[r_][c_+1] == "]"):
                    print()
                    br = True
        if br:
            print(idx)
            for row in grid:
                print("".join(row))
            break
    res = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "[":
                res += r*100 + c

    #final grid
    for row in grid:
        print("".join(row))
    print(res)

#part1(input_grid, directions)
part2(expanded_grid, directions)

#getting fired if my manager ever sees this level of code
