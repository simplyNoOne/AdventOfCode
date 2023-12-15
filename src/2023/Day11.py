
def day11_base():
    with open('inputs/day11.txt') as f:
        small_universe = []
        while line := f.readline():
            small_universe.append(line.split("\n")[0])
            if line.find('#') == -1:
                small_universe.append(line.split("\n")[0])

    universe = []
    for _ in small_universe:
        universe.append([])

    for i in range(len(small_universe[0])):
        empty = True
        for j in range(len(small_universe)):
            if small_universe[j][i] == '#':
                empty = False
                break
        for j in range(len(small_universe)):
            universe[j].append(small_universe[j][i])
            if empty:
                universe[j].append(small_universe[j][i])

    galaxies = []
    for i, row in enumerate(universe):
        for j, g in enumerate(row):
            if g == '#':
                galaxies.append((i, j))

    distance = 0
    for i in range(len(galaxies)):
        for j in range (i+1, len(galaxies)):
            distance += abs(galaxies[i][0] - galaxies[j][0])
            distance += abs(galaxies[i][1] - galaxies[j][1])

    return distance


def day11_extra():
    with open('inputs/day11.txt') as f:
        universe = []
        empty_rows = []
        index = 0
        while line := f.readline():
            universe.append(line.split("\n")[0])
            if line.find('#') == -1:
                empty_rows.append(index)
            index += 1

    empty_cols = []
    for i in range(len(universe[0])):
        empty = True
        for j in range(len(universe)):
            if universe[j][i] == '#':
                empty = False
                break
        if empty:
            empty_cols.append(i)

    galaxies = []
    for i, row in enumerate(universe):
        for j, g in enumerate(row):
            if g == '#':
                galaxies.append((i, j))

    distance = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            empty_c = 0
            empty_r = 0
            for e in empty_cols:
                if galaxies[i][1] < e < galaxies[j][1] or galaxies[i][1] > e > galaxies[j][1]:
                    empty_c += 1
            for e in empty_rows:
                if galaxies[i][0] < e < galaxies[j][0] or galaxies[i][0] > e > galaxies[j][0]:
                    empty_r += 1

            distance += abs(galaxies[i][0] - galaxies[j][0])
            distance += abs(galaxies[i][1] - galaxies[j][1])
            distance += (empty_c + empty_r) * 999999

    return distance
