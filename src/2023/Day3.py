

def day3_base():
    f = open('inputs/day3.txt', 'r')
    line = f.readline()
    line_len = len(line)

    visit_map = [[False] * line_len for _ in range(140)]
    result = 0
    line_ct = 0
    prevl = line
    line = f.readline()
    nextl = f.readline()
    while True:
        lines = [prevl, line, nextl]
        if not nextl:
            break
        for i, c in enumerate(line):
            if c.isdigit() or c == '.':
                continue
            if i == 0 or i == line_len - 1:
                continue
            else:
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if not visit_map[line_ct + j][i + k]:
                            result += spread(lines[1 + j], i + k, line_ct + j, visit_map)
        line_ct += 1
        prevl = line
        line = nextl
        nextl = f.readline()
    f.close()
    return result


def spread(line, x, y, v_map):
    v_map[y][x] = True
    if not line[x].isdigit():
        return 0
    num = int(line[x])
    i = 1
    keep_l = True
    keep_r = True
    while x >= i and x + i < len(line) and (line[x-i].isdigit() or line[x+i].isdigit()):
        if not keep_r and not keep_l:
            break
        if keep_l and line[x-i].isdigit():
            num += (10 ** i) * int(line[x - i])
            v_map[y][x - i] = True
        else:
            keep_l = False
        if keep_r and line[x + i].isdigit():
            num = num*10 + int(line[x + i])
            v_map[y][x + i] = True
        else:
            keep_r = False
        i += 1
    return num



def day3_extra():
    f = open('inputs/day3.txt', 'r')
    line = f.readline()
    line_len = len(line)

    visit_map = [[False] * line_len for _ in range(140)]
    result = 0
    line_ct = 0
    prevl = line
    line = f.readline()
    nextl = f.readline()
    while True:
        lines = [prevl, line, nextl]
        if not nextl:
            break
        for i, c in enumerate(line):
            if i == 0 or i == line_len - 1:
                continue
            if c != '*':
                continue
            else:
                ratio = 1
                counter = 0
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if not visit_map[line_ct + j][i + k]:
                            num = spread(lines[1 + j], i + k, line_ct + j, visit_map)
                            if num != 0:
                                counter += 1
                                ratio *= num
                if counter == 2:
                    result += ratio
        line_ct += 1
        prevl = line
        line = nextl
        nextl = f.readline()
    f.close()
    return result
