with open("input4.txt") as f:
    data = f.read().splitlines()

s = "XMAS"
res = 0
res2 = 0
rows, cols = len(data), len(data[0])
for r in range(rows):
    for c in range(cols):
        for dr, dc in [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1],
            [1,1],
            [1,-1],
            [-1,1],
            [-1,-1],
        ]:
            matched = True
            for i in range(len(s)):
                nr, nc = r + i*dr, c + i*dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    matched = False
                    break
                if s[i] != data[nr][nc]:
                    matched = False
                    break
            res += matched

        patterns = [
            ["M.S", ".A.", "M.S"],
            ["M.M", ".A.", "S.S"],
            ["S.S", ".A.", "M.M"],
            ["S.M", ".A.", "S.M"],
            ]
        for i in range(4):
            m = True
            for dr in range(3):
                for dc in range(3):
                    if patterns[i][dr][dc] == ".":
                        continue
                    else:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                            m = False
                            continue
                        if patterns[i][dr][dc] != data[nr][nc]:
                            m = False
            
            res2 += m
print(res2)


