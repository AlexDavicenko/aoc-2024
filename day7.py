DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()

def part1():
    res = 0
    for line in data.splitlines():
        ans, operands = line.split(": ")
        operands = list(map(int, operands.split(" ")))
        possible = False
        for i in range(1<<(len(operands)-1)):
            s = operands[0]
            for j in range(len(operands)-1):
                if (i>>j)&1:
                    s *= operands[j+1] 
                else:
                    s += operands[j+1] 
            if s == int(ans):
                possible = True

        if possible: 
            res += int(ans)
    return res
    
#print(part1())

def part2():
    res = 0
    for line in data.splitlines():
        ans, operands = line.split(": ")
        operands = list(map(int, operands.split(" ")))
        possible = False
        for i in range(3**(len(operands)-1)):
            s = operands[0]
            for j in range(len(operands)-1):
                if (i//(3**j))%3 == 0:
                    s = int(str(s)+str(operands[j+1]))
                if (i//(3**j))%3 == 1:
                    s *= operands[j+1] 
                if (i//(3**j))%3 == 2:
                    s += operands[j+1]
            #print(f"line: {operands} sum: {s}")
            if s == int(ans):
                possible = True

        if possible: 
            res += int(ans)
            print(line)
    return res
print(part2())