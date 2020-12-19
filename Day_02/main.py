def result(grid, pos):
    code = ""

    for line in lines:
        for letter in line:
            if letter == 'U':
                newpos = (pos[0], pos[1] - 1)
            elif letter == 'D':
                newpos = (pos[0], pos[1] + 1)
            elif letter == 'R':
                newpos = (pos[0] + 1, pos[1])
            elif letter == 'L':
                newpos = (pos[0] - 1, pos[1])
            if grid[newpos[0]][newpos[1]] != 0:
                pos = newpos
        int = grid[pos[0]][pos[1]]
        char = str(grid[pos[0]][pos[1]])
        if int == 10:
            char = 'A'
        elif int == 11:
            char = 'B'
        elif int == 12:
            char = 'C'
        elif int == 13:
            char = 'D'
        code += char

    return code


with open("input.txt") as f:
    lines = f.readlines()

pos = (2, 2)
grid = [[0, 0, 0, 0, 0], [0, 1, 4, 7, 0], [0, 2, 5, 8, 0], [0, 3, 6, 9, 0], [0, 0, 0, 0, 0]]
print("Answer part 1:", result(grid, pos))

pos = (3, 3)
grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 5, 0, 0, 0], [0, 0, 2, 6, 10, 0, 0], [0, 1, 3, 7, 11, 13, 0], [0, 0, 4, 8, 12, 0, 0], [0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
print("Answer part 2:", result(grid, pos))
