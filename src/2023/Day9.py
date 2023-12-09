

def day9_base():
    histories = []
    with open('inputs/day9.txt') as f:
        while line := f.readline():
            histories.append([int(val) for val in line.split("\n")[0].split(' ')])
    print(histories)
    total = 0
    for history in histories:
        dive = [history]
        level = history
        while not dive_ready(dive):
            diffs = []
            for i in range(1, len(level)):
                diffs.append(level[i] - level[i-1])
            dive.append(diffs)
            level = diffs
        sum_d = 0
        dive[-1].append(0)
        for i in range(len(dive) - 1, -1, -1):
            sum_d += dive[i][-1]
        total += sum_d
    return total


def dive_ready(dive):
    if len(dive) == 0:
        return False
    for d in dive[-1]:
        if d != 0: return False
    return True


def day9_extra():
    histories = []
    with open('inputs/day9.txt') as f:
        while line := f.readline():
            histories.append([int(val) for val in line.split("\n")[0].split(' ')])
    print(histories)
    total = 0
    for history in histories:
        dive = [history]
        level = history
        while not dive_ready(dive):
            diffs = []
            for i in range(1, len(level)):
                diffs.append(level[i] - level[i-1])
            dive.append(diffs)
            level = diffs
        dive[-1].append(0)
        prev = 0
        for i in range(len(dive) - 1, -1, -1):
            prev = dive[i][0] - prev
        total += prev
    return total
