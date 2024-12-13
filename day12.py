from collections import defaultdict
DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()

grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])

visited = set()
res = 0
perim_sets = []
wall_mp = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        if (r,c) in visited: continue
        area = 0
        perim = 0
        stack = [(r,c)]
        nodes = []
        visited.add((r,c))
        while stack:
            cr, cc = stack.pop()
            nodes.append((cr, cc))
            area += 1
            for dr, dc in [
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            ]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr and nr < rows and 0 <= nc and nc < cols:
                    if grid[nr][nc] != grid[r][c]:
                            perim += 1
                            wall_mp[(cr, cc)].append((dr,dc))
                    if (nr,nc) not in visited:
                        if grid[nr][nc] == grid[r][c]:
                            visited.add((nr,nc))
                            stack.append((nr,nc))
                else:
                    perim += 1
                    wall_mp[(cr, cc)].append((dr,dc))
        perim_sets.append((nodes, area))
for nodes, area in perim_sets:
    nodes_set = set(nodes)
    walls = 0
    idx = 0
    for i, n in enumerate(nodes):
        if not wall_mp[n]: continue
        #print(f"rm {wall_mp[(3,0)]}")
        r, c = n
        for dr, dc in wall_mp[n]:
            #print(r,c,dr,dc)
            if dc == 0:
                for c_i in range(c+1,cols):
                    if (r,c_i) in nodes_set:
                        if (dr, dc) in wall_mp[(r,c_i)]:
                            print((dr,dc))
                            wall_mp[(r,c_i)].remove((dr,dc))
                        else:
                            break
                    else:
                        break
                for c_i in range(c-1,-1,-1):
                    if (r,c_i) in nodes_set:
                        if (dr, dc) in wall_mp[(r,c_i)]:
                            print((dr,dc))
                            wall_mp[(r,c_i)].remove((dr,dc))
                        else:
                            break
                    else:
                        break
            if dr == 0:
                for r_i in range(r+1,rows):
                    if (r_i,c) in nodes_set:
                        if (dr, dc) in wall_mp[(r_i,c)]:
                            print((dr,dc))
                            wall_mp[(r_i,c)].remove((dr,dc))
                        else:
                            break
                    else:
                        break
                for r_i in range(r-1,-1,-1):
                    if (r_i,c) in nodes_set:
                        if (dr, dc) in wall_mp[(r_i,c)]:
                            print((dr,dc))
                            wall_mp[(r_i,c)].remove((dr,dc))
                        else:
                            break
                    else:
                        break
            
            walls += 1 
        wall_mp[n] = []
                
    res += area * walls

print(res)
