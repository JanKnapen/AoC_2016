import hashlib


def part1(string):
    returned = ""
    i = 0
    j = 0
    while i < 8:
        str2 = string + str(j)
        result = hashlib.md5(str2.encode()).hexdigest()
        if result[0:5] == "00000":
            i += 1
            returned += result[5]
        j += 1
    return returned


def part2(string):
    valid = ["0", "1", "2", "3", "4", "5", "6", "7"]
    included = []
    letters = []
    i = 0
    j = 0
    while i < 8:
        str2 = string + str(j)
        result = hashlib.md5(str2.encode()).hexdigest()
        if result[0:5] == "00000" and result[5] in valid and result[5] not in included:
            i += 1
            included.append(result[5])
            letters.append((result[5], result[6]))
        j += 1

    returned = ""
    for k in range(8):
        tuples = [y for (x, y) in letters if x == str(k)]
        returned += tuples[0]
    return returned


input = "ffykfhsq"

print("Answer part 1:", part1(input))
print("Answer part 2:", part2(input))
