with open("input3.txt") as f:
    data = f.read()


idx = 0 
res = 0
on = 1
while idx < len(data):
    if data[idx:idx+7] == "don't()":
        on = 0
    if data[idx:idx+4] == "do()":
        on = 1
    if data[idx:idx+4] == "mul(":
        j = idx + 4
        left = ''
        while j < len(data) and data[j].isdigit():
            left += data[j]
            j += 1
        if data[j] == ",":
            j += 1
            right = ''
            while j < len(data) and data[j].isdigit():
                right += data[j]
                j += 1
            if data[j] == ")":
                res += int(left) * int(right) * on
                print(left, right)
                idx = j
    idx += 1
print(res)