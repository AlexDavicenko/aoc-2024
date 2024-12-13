from collections import Counter

with open("input1.txt") as f:
    data = f.read()


arr1, arr2 = [], []
for line in data.splitlines():
    print(line)
    x, y = line.split("   ")
    arr1.append(int(x))
    arr2.append(int(y))
arr1.sort()
arr2.sort()
res = 0
for i in range(len(arr1)):
    res += abs(arr1[i]-arr2[i])
print(res)

res2 = 0
counter = Counter(arr2)
for v in arr1:
    res2 += v*counter[v]
print(res2)