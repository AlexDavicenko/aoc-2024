DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()
from collections import defaultdict
arr = list(map(int, data))
n = sum(arr)
mem = [-1]*n
count = 0
ids = 0
for i in range(len(arr)):
    if i % 2:
        #skip
        pass
    else:
        for j in range(arr[i]):
            mem[count+j] = ids
        
        ids += 1
    count += arr[i]

L = 0
R = n-1
#print(mem)
while L < R:
    
    while mem[L] != -1:
        L += 1
    while mem[R] == -1:
        R += -1
    if L >= R: break
    mem[L], mem[R] = mem[R], mem[L]
    R += -1
    #print(L, R, "".join(map(str,mem)).replace("-1", "."))

res = 0
for i in range(n):
    if mem[i] != -1:
        res += i*mem[i]
print(res)
print(arr)

mp = []
count = 0
for i in range(len(arr)):
    if i % 2:
        mp.append([arr[i], -1])
    else:
        mp.append([arr[i], count])
        count += 1
print(mp)

block_mp = defaultdict(list)
for i in range(len(mp)-1,-1,-1):
    if mp[i][1] < 0:
        continue

    for j in range(i):
        if mp[j][1] < 0:
            if mp[j][0] >= mp[i][0]:
                mp[j][0] = mp[j][0] - mp[i][0]
                block_mp[j].append(mp[i].copy())
                mp[i][1] = -1
                break
print(mp)
print(block_mp)

count = 0
res_2 = 0
for i in range(len(mp)):
    for j in range(len(block_mp[i])):
        for k in range(block_mp[i][j][0]):
            res_2 += (count + k) * block_mp[i][j][1]
        count += block_mp[i][j][0]
    if mp[i][1] >= 0:
        for k in range(mp[i][0]):
            res_2 += (count + k) * mp[i][1]
    count += mp[i][0]

print(res_2)
