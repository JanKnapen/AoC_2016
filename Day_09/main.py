def part1():
    line1 = line.split()
    i = 0
    res = ""
    length = 0
    total = 0
    repeat = ""
    while i < len(line1):
        if length > 0:
            if length > len(line1[i]):
                length -= len(line1[i])
                repeat += line1[i]
            else:
                repeat += line1[i][0:length]
                res += total * repeat
                total = 0
                repeat = ""
                res += line1[i][length:len(line1[i])]
                length = 0
        elif line1[i].startswith("("):
            length = int(line1[i][1:-1].split("x")[0])
            total = int(line1[i][1:-1].split("x")[1])
        else:
            res += line1[i]
        i += 1
    return len(res)


def dec(str):
    if "(" not in str:
        return len(str)
    length = 0
    while "(" in str:
        length += str.find("(")
        str = str[str.find("("):]
        marker = str[1:str.find(")")].split("x")
        str = str[str.find(")") + 1:]
        length += dec(str[:int(marker[0])]) * int(marker[1])
        str = str[int(marker[0]):]
    length += len(str)
    return length


with open("input.txt") as f:
    lines = f.readlines()

line = lines[0].replace(")", ") ").replace("(", " (").replace("  ", " ")

print("Answer part 1:", part1())
print("Answer part 2:", dec(lines[0]))
