from collections import defaultdict
with open("input5.txt", "r") as f: 
    prereqs, orderings = f.read().split("\n\n")

graph = defaultdict(set)
for line in prereqs.splitlines():
    u, v = line.split("|")
    graph[v].add(u)

res = 0
for ordering in orderings.splitlines():
    ordering = ordering.split(",")
    possible = True
    for i in range(len(ordering)-1,-1,-1):
        u = ordering[i]
        #graph[u] is all the nodes that must appear before u in the ordering
        #banned must be before v
        banned = set()
        stack = [u]
        visited = set([u])
        while stack:
            k = stack.pop()
            banned.add(k)
            for t in graph[k]:
                if t not in visited:
                    stack.append(t)
                    visited.add(t)
        print(banned)
        for j in range(i-1, -1, -1):
            v = ordering[j]
            if v not in banned:
                possible = False
                break
        if not possible: break
    
    if possible:
        res += int(ordering[len(ordering)//2])
print(res)
for r in graph:
    print(len(graph[r]))
