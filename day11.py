from collections import Counter

DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()

stones = list(map(int, data.split()))
counter = Counter(stones)

from time import perf_counter
stime = perf_counter()
iters = 10000
for i in range(iters):
    new_counter = Counter()
    
    for s, count in counter.items():
        if s == 0: 
            new_counter[1] += count
        elif len(str(s)) % 2 == 0:
            s_str = str(s)
            new_counter[int(s_str[:len(s_str)//2])] += count
            new_counter[int(s_str[len(s_str)//2:])] += count
        else:
            new_counter[2024*s] += count

    counter = new_counter
print(len(counter))
print(sum(counter.values()))
print(perf_counter()-stime)