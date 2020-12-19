import collections


def get_message(part):
    dict = {}
    for line in lines:
        for i in range(len(line)):
            if i not in dict:
                dict[i] = [line[i]]
            else:
                dict[i].append(line[i])
    result = ""
    for i in dict:
        result += collections.Counter(dict[i]).most_common()[-(part-1)][0]
    return result[0:-1]


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", get_message(1))
print("Answer part 2:", get_message(2))
