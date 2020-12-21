import numpy as np


def part1():
    for line in lines:
        line = line.split()
        op = line[0]
        if op == "rect":
            width = int(line[1].split("x")[0])
            height = int(line[1].split("x")[1])
            for y in range(height):
                for x in range(width):
                    on[y][x] = 1
        elif op == "rotate":
            if line[1] == "row":
                row = int(line[2].split("=")[1])
                steps = int(line[4])
                rolled = np.roll(on, steps, axis=1)
                on[row] = rolled[row]
            elif line[1] == "column":
                column = int(line[2].split("=")[1])
                steps = int(line[4])
                rolled = np.roll(on, steps, axis=0)
                for i in range(6):
                    on[i][column] = rolled[i][column]

    count = 0
    for y in range(on.shape[0]):
        for x in range(on.shape[1]):
            count += on[y][x]
    return int(count)


with open("input.txt") as f:
    lines = f.readlines()

on = np.zeros((6, 50))

print("Answer part 1:", part1())
