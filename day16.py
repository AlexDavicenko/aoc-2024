DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()
from heapq import *
from collections import defaultdict
input_grid = list(map(list, data.splitlines()))

DIRECTIONS = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]

def part1(grid):
    rows = len(grid)
    cols = len(grid[0])

    heap = []
    dist = defaultdict(lambda : (1<<31)-1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                dist[(row, col, 0, 1)] = 0
                heap.append((0,0,1,row,col))
    from_mp = defaultdict(list)
    while heap:
        cost, dr, dc, r, c = heappop(heap)

        moves = [
            (1, r+dr,c+dc)
        ]
        moves.append((2001,r-dr,c-dc))
        if dr == 0:
            moves.append((1001, r+1, c))
            moves.append((1001, r-1, c))
        if dc == 0:
            moves.append((1001, r, c+1))
            moves.append((1001, r, c-1))
        for inc_cost, nr, nc in moves:
            if grid[nr][nc] == "#": continue
            n_dr, n_dc = nr-r, nc-c
            add = False
            new_state = nr,nc,n_dr, n_dc
            old_state = r, c, dr, dc
            if (new_state) in dist:
                if dist[new_state] > dist[old_state] + inc_cost:
                    add = True
                    dist[new_state] = dist[old_state] + inc_cost
                    from_mp[new_state] = [old_state]
                elif dist[new_state] == dist[old_state] + inc_cost:
                    add = True
                    from_mp[new_state].append(old_state)

            else:
                add = True
                from_mp[new_state].append(old_state)

            if add:
                dist[new_state] = dist[old_state] + inc_cost
                heappush(heap, (cost+inc_cost, nr-r, nc-c, nr, nc))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "E":


                if dist[(row, col, -1, 0)] < dist[(row, col, 0, 1)]:
                    stack = [(row,col, -1, 0)]
                else:
                    stack = [(row,col, 0, 1)]
                visited = set(stack)
                while stack:
                    state = stack.pop()
                    grid[state[0]][state[1]] = "O"

                    for prev_state in from_mp[state]:
                        if prev_state not in visited:
                            visited.add(prev_state)
                            stack.append(prev_state)
                res2 = 0
                for row in range(rows):
                    for col in range(cols):
                        if grid[row][col] == "O":
                            res2 +=  1
                        #print(grid[row][col], end="")
                        #print(f"({row}, {col}): {grid[row][col]}", end="| ")
                    #print()

                print(res2)

part1(input_grid)