def part1():
    pos = (0, 0)
    dir = (0, 1)

    for com in coms:
        if com[0] == 'L':
            dir = (-1*dir[::-1][0], dir[::-1][1])
        if com[0] == 'R':
            dir = (dir[::-1][0], -1*dir[::-1][1])
        dis = int(com[1:len(com)])
        pos = (pos[0]+dis*dir[0], pos[1]+dis*dir[1])

    return abs(pos[0]) + abs(pos[1])

def part2():
    pos = (0,0)
    dir = (0,1)
    visited = [(0,0)]

    class Found(Exception): pass
    try:
        for com in coms:
            if com[0] == 'L':
                dir = (-1*dir[::-1][0], dir[::-1][1])
            if com[0] == 'R':
                dir = (dir[::-1][0], -1*dir[::-1][1])
            dis = int(com[1:len(com)])
            newpos = (pos[0]+dis*dir[0], pos[1]+dis*dir[1])
            visited.remove(pos)
            for x in range(abs(newpos[0] - pos[0]) + 1):
                for y in range(abs(newpos[1] - pos[1]) + 1):
                    temppos = (pos[0]+dir[0]*x, pos[1]+dir[1]*y)
                    if temppos in visited:
                        visited.append(temppos)
                        raise Found
                    visited.append(temppos)
            pos = newpos
    except Found:
        return abs(visited[-1][0]) + abs(visited[-1][1])


with open("input.txt") as f:
    lines = f.readlines()

coms = lines[0].split(", ")

print("Answer part 1:", part1())
print("Answer part 2:", part2())
