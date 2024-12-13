from collections import defaultdict
DAY = __file__.split("\\")[-1].split(".")[0][3:]
with open(f"input{DAY}.txt", "r") as f:
    data = f.read()
import numpy as np
from fractions import Fraction

machines = data.split("\n\n")

res = 0
def matrix_inv(a,b,c,d):
    det = a*d-b*c
    return d/det, -b/det, -c/det, a/det
INCREASE = 10000000000000
def button_parse(line):
    return int(line.split(": ")[1].split(",")[0].split("+")[1]), int(line.split(": ")[1].split(",")[1].split("+")[1])
for machine in machines:
    machine = machine.splitlines()
    prize_line = machine[2]
    prize_x, prize_y = prize_line.split(": ")[1].split(", ")
    prize_x = int(prize_x.split("=")[1]) + INCREASE
    prize_y = int(prize_y.split("=")[1]) + INCREASE

    A_x, A_y = button_parse(machine[0])
    B_x, B_y = button_parse(machine[1])
    #print(A_x, A_y)
    #print(B_x, B_y)
    #print(prize_x, prize_y)
    """
    mn = (1<<31)-1
    lim = 10000
    for a_count in range(lim+1):
        for b_count in range(lim+1):
            if A_x*a_count + B_x * b_count == prize_x and A_y*a_count + B_y*b_count == prize_y:
                mn = min(mn, 3*a_count+b_count)
    res += mn if mn != (1<<31)-1 else 0
    """
    mat = np.array([
        [A_x, B_x],
        [A_y, B_y]
    ], dtype=Fraction)

    inv = np.array(matrix_inv(Fraction(A_x), Fraction(B_x), Fraction(A_y), Fraction(B_y))).reshape((2,2))
    vec = np.array([prize_x, prize_y], dtype=Fraction)
    
    sol = inv@vec
    a_count, b_count = sol
    if a_count.denominator == 1 and b_count.denominator == 1:
        #print(3*a_count+b_count)
        res += 3*a_count+b_count
    #a*A_x + b*B_x = prize_x
    #a*A_y + b*B_y = prize_y
    #
print(res)