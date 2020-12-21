def part1():
    i = 0
    res = ""
    length = 0
    total = 0
    repeat = ""
    while i < len(line):
        if length > 0:
            if length > len(line[i]):
                length -= len(line[i])
                repeat += line[i]
            else:
                repeat += line[i][0:length]
                res += total * repeat
                total = 0
                repeat = ""
                res += line[i][length:len(line[i])]
                length = 0
        elif line[i].startswith("("):
            length = int(line[i][1:-1].split("x")[0])
            total = int(line[i][1:-1].split("x")[1])
        else:
            res += line[i]
        i += 1
    return len(res)


with open("input.txt") as f:
    lines = f.readlines()

line = lines[0].replace(")", ") ").replace("(", " (").replace("  ", " ").split()

print("Answer part 1:", part1())
