def is_triangle(sides):
    if sides[0] + sides[1] <= sides[2] or sides[0] + sides[2] <= sides[1] \
            or sides[1] + sides[2] <= sides[0]:
        return False
    return True


def part1():
    count = 0
    for triangle in lines:
        sides = triangle.split()
        if is_triangle([int(sides[0]), int(sides[1]), int(sides[2])]):
            count += 1
    return count


def part2():
    count = 0
    for i in range(len(lines)):
        if i % 3 == 0:
            sides_1 = lines[i].split()
            sides_2 = lines[i+1].split()
            sides_3 = lines[i+2].split()
            for j in range(3):
                if is_triangle([int(sides_1[j]), int(sides_2[j]), int(sides_3[j])]):
                    count += 1
            i += 3
    return count


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", part1())
print("Answer part 2:", part2())
