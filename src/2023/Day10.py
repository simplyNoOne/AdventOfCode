import math


def day10_base():

    r_side = {'L': (-1, 0, 2), 'F': (1, 0, 0), '-': (0, -1, 1), 'S': (0, 0, 0)}
    l_side = {'J': (-1, 0, 2), '7': (1, 0, 0), '-': (0, 1, 3), 'S': (0, 0, 0)}
    u_side = {'L': (0, 1, 3), 'J': (0, -1, 1), '|': (1, 0, 0), 'S': (0, 0, 0) }
    d_side = {'7': (0, -1, 1), 'F': (0, 1, 3), '|': (-1, 0, 2), 'S': (0, 0, 0) }
    moves = [u_side, r_side, d_side, l_side]

    with open('inputs/day10.txt') as f:
        grid = []
        s = (-1, -1)
        while line := f.readline():
            grid.append(line.split("\n")[0])
            if s[1] == -1:
                s = (s[0] + 1, line.find('S'))

    def find_start(start_id):
        if start_id[0] > 0:
            if grid[start_id[0] - 1][start_id[1]] == 'F' or '7':
                return start_id[0] - 1, start_id[1], 2
        elif start_id[1] < len(grid[0]) - 1:
            if grid[start_id[0]][start_id[1] + 1] == 'J' or '7':
                return start_id[0], start_id[1] + 1, 3
        else:
            return start_id[0] + 1, start_id[1], 0

    def get_next(start):
        next_move = start
        path_len = 0
        while True:
            path_len += 1
            new_dir = moves[next_move[2]][grid[next_move[0]][next_move[1]]]
            if new_dir == (0, 0, 0):
                return path_len
            next_move = (next_move[0] + new_dir[0], next_move[1] + new_dir[1], new_dir[2])

    return math.ceil(get_next(find_start(s))/2)


def day10_extra():

    r_side = {'L': (-1, 0, 2), 'F': (1, 0, 0), '-': (0, -1, 1), 'S': (0, 0, 0)}
    l_side = {'J': (-1, 0, 2), '7': (1, 0, 0), '-': (0, 1, 3), 'S': (0, 0, 0)}
    u_side = {'L': (0, 1, 3), 'J': (0, -1, 1), '|': (1, 0, 0), 'S': (0, 0, 0) }
    d_side = {'7': (0, -1, 1), 'F': (0, 1, 3), '|': (-1, 0, 2), 'S': (0, 0, 0) }
    moves = [u_side, r_side, d_side, l_side]

    with open('inputs/day10.txt') as f:
        grid = []
        s = (-1, -1)
        while line := f.readline():
            grid.append(line.split("\n")[0])
            if s[1] == -1:
                s = (s[0] + 1, line.find('S'))

    def find_start(start_id):
        if start_id[0] > 0:
            if grid[start_id[0] - 1][start_id[1]] == 'F' or '7':
                return start_id[0] - 1, start_id[1], 2
        elif start_id[1] < len(grid[0]) - 1:
            if grid[start_id[0]][start_id[1] + 1] == 'J' or '7':
                return start_id[0], start_id[1] + 1, 3
        else:
            return start_id[0] + 1, start_id[1], 0

    is_path = []
    check_vert = []
    check_hor = []
    for _ in grid:
        is_path.append([(False, 0)] * len(grid[0]))
        check_hor.append([False] * len(grid[0]))
        check_vert.append([False] * len(grid[0]))
    is_path[s[0]][s[1]] = (True, 0)

    def mark_path(start):
        next_move = start
        path_len = 0
        while True:
            is_path[next_move[0]][next_move[1]] = (True, next_move[2] % 2)
            path_len += 1
            new_dir = moves[next_move[2]][grid[next_move[0]][next_move[1]]]
            if new_dir == (0, 0, 0):
                return
            next_move = (next_move[0] + new_dir[0], next_move[1] + new_dir[1], new_dir[2])

    mark_path(find_start(s))

    for a in is_path:
        print (a)

    for i, row in enumerate(is_path):
        inside = False
        was_hor = False
        for j, cell in enumerate(row):
            if is_path[i][j][0] and is_path[i][j][1] != 1:
                if not was_hor:
                    inside = not inside
                was_hor = False
            elif not is_path[i][j][0]:
                if was_hor:
                    inside = not inside
                    was_hor = False
                check_hor[i][j] = inside
            else:
                was_hor = True

    for i in range(len(is_path[0])):
        inside = False
        was_vert = False
        for j in range(len(is_path)):
            if is_path[j][i] and is_path[j][i][1] != 0:
                if not was_vert:
                    inside = not inside
                was_vert = False
            elif not is_path[j][i][0]:
                if was_vert:
                    inside = not inside
                    was_vert = False
                check_vert[j][i] = inside
            else:
                was_vert = True

    print("vert")
    for a in check_vert:
        print (a)

    print("hor")
    for a in check_hor:
        print(a)

    area = 0
    for v_row, h_row in zip(check_vert, check_hor):
        for v, h in zip(v_row, h_row):
            if v and h:
                area += 1

    return area


