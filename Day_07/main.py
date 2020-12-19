def is_abba(str):
    if len(str) != 4:
        return False
    if str[0] != str[1] and str[0] == str[3] and str[1] == str[2]:
        return True
    return False


def is_valid_1(str):
    i = 0
    contains = False
    for word in str.replace("[", "]").split("]"):
        j = 0
        while j + 3 < len(word):
            if is_abba(word[j:j+4]):
                if i % 2 == 0:
                    contains = True
                else:
                    return False
            j += 1
        i += 1
    return contains


def part1():
    count = 0
    for line in lines:
        if is_valid_1(line):
            count += 1
    return count


def is_aba(str):
    if len(str) != 3:
        return False
    if str[0] != str[1] and str[0] == str[2]:
        return True
    return False


def is_valid_2(str):
    i = 0
    aba = []
    bab = []
    for word in str.replace("[", "]").split("]"):
        j = 0
        while j + 2 < len(word):
            if is_aba(word[j:j+3]):
                if i % 2 == 0:
                    aba.append(word[j:j+3])
                else:
                    bab.append(word[j:j+3])
            j += 1
        i += 1
    for aba_word in aba:
        for bab_word in bab:
            if aba_word[0] == bab_word[1] and aba_word[1] == bab_word[0]:
                return True
    return False


def part2():
    count = 0
    for line in lines:
        if is_valid_2(line):
            count += 1
    return count


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", part1())
print("Answer part 2:", part2())
