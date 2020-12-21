with open("input.txt") as f:
    lines = f.readlines()

dict = {}
for line in lines:
    if "goes" in line:
        line = line.split()
        val = int(line[1])
        bot = int(line[5])
        if bot in dict.keys():
            dict[bot].append(val)
        else:
            dict[bot] = [val]

q = []
for key in dict.keys():
    if len(dict[key]) > 1:
        q.append(key)

output = {}
while len(q) > 0:
    bot = q.pop(0)
    for line in lines:
        line = line.split()
        if "gives" in line and int(line[1]) == bot:
            low = int(line[6])
            high = int(line[11])
            if line[5] == "output":
                output[low] = min(dict[bot])
            else:
                if low in dict.keys():
                    dict[low].append(min(dict[bot]))
                    q.append(low)
                else:
                    dict[low] = [min(dict[bot])]
            if line[10] == "output":
                output[high] = max(dict[bot])
            else:
                if high in dict.keys():
                    dict[high].append(max(dict[bot]))
                    q.append(high)
                else:
                    dict[high] = [max(dict[bot])]

bot = 0
for key in dict.keys():
    if 61 in dict[key] and 17 in dict[key]:
        bot = key

print("Answer part 1:", bot)
print("Answer part 2:", output[0] * output[1] * output[2])
