with open("input2.txt") as f:
    data = f.read()
res = 0
for line in data.splitlines():
    arr = list(map(int, line.split(" ")))
    print(arr)
    possible_safe = False
    for j in range(len(arr)):
        rm = arr.pop(j)
        safe = True
        sign = (arr[1]-arr[0]) < 0
        for i in range(len(arr)-1):
            if 1 > abs(arr[i+1] - arr[i]) or abs(arr[i+1] - arr[i]) > 3:
                safe = False
            new_sign = (arr[i+1] - arr[i]) < 0
            if sign != new_sign:
                safe = False
        if safe:
            possible_safe = True
        arr.insert(j, rm)
    if possible_safe: res += 1

    
print(res)