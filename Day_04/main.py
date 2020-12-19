import collections


def patched_most_common(self):
    return sorted(self.items(), key=lambda x: (-x[1], x[0]))


def next_char(char, steps=1):
    steps = steps%26
    return chr((ord(char)-97 + steps)%26+97)


def valid(str, checksum):
    total = 0
    for letter in collections.Counter(str).most_common():
        if letter[0] not in checksum:
            return False
        total += 1
        if total == 5:
            return True
    return False


def valid_data():
    data = []

    for line in lines:
        names = line.split("-")[0:-1]
        id = line.split("-")[len(line.split("-"))-1].split("[")[0]
        checksum = line.split("-")[len(line.split("-"))-1].split("[")[1][0:-2]
        str = ""
        for name in names:
            str += name
        if valid(str, checksum):
            returned = ""
            for name in names:
                returned += "-" + name
            data.append((returned[1::], id))
    return data


def part1():
    sum = 0
    for tuple in valid_data():
        sum += int(tuple[1])

    return sum


def part2():
    for tuple in valid_data():
        real_name = ""
        for letter in tuple[0]:
            if letter != "-":
                real_name += next_char(letter, int(tuple[1]))
            else:
                real_name += " "
        if real_name == "northpole object storage":
            return tuple[1]
    return -1


with open("input.txt") as f:
    lines = f.readlines()

collections.Counter.most_common = patched_most_common

print("Answer part 1:", part1())
print("Answer part 2:", part2())
