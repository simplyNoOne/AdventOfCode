import string
from collections import deque


def calc_path(start, end, grid):
    visited = []
    queue = deque([[start]])
    while True:
        if len(queue) == 0:
            return None
        path = queue.popleft()
        pos = path[-1]
        if pos == end:
            return path
        for x, y in ((pos[0] -1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)):
            if 0<= x < len(grid) and 0<= y < len(grid[0]):
                if grid[x][y] <= grid[pos[0]][pos[1]] + 1 and [x, y] not in visited:
                    queue.append(path + [[x, y]])
                    visited.append([x, y])


def day12_base():
    f = open('../inputs/day12.txt', 'r')
    buffer = f.read().split('\n')
    f.close()
    buffer.pop()

    grid = []
    start = []
    end = []
    letters = string.ascii_lowercase
    for r in range(len(buffer)):
        grid.append([])
        for l in range(len(buffer[0])):
            if buffer[r][l] == 'S':
                start = [r, l]
                grid[-1].append(0)
            elif buffer[r][l] == 'E':
                end = [r, l]
                grid[-1].append(letters.index('z'))
            else:
                grid[-1].append(letters.index(buffer[r][l]))

    print("Shortest path requires " + str(len(calc_path(start, end, grid)) - 1) + " steps")


def day12_extra():
    f = open('../inputs/day12.txt', 'r')
    buffer = f.read().split('\n')
    f.close()
    buffer.pop()
    paths = []
    grid = []
    start = []
    end = []
    letters = string.ascii_lowercase
    for r in range(len(buffer)):
        grid.append([])
        for l in range(len(buffer[0])):
            if buffer[r][l] == 'S' or buffer[r][l] == 'a':
                start.append([r, l])
                grid[-1].append(0)
            elif buffer[r][l] == 'E':
                end = [r, l]
                grid[-1].append(letters.index('z'))
            else:
                grid[-1].append(letters.index(buffer[r][l]))
    for s in start:
        x = calc_path(s, end, grid)
        if x:
            paths.append(x)
    min_steps = 999
    for p in paths:
        if len(p) < min_steps:
            min_steps = len(p)

    print("Shortest path overall requires " + str(min_steps - 1) + " steps")

