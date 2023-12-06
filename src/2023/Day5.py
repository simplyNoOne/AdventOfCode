import re

def day5_base():
    with open('inputs/day5.txt', 'r') as f:
        grid = f.read()

    grid = [token for token in re.split(r'[:\n\s]', grid) if token != '']
    conversions = [[]]
    for g in grid:
        if not g[0].isdigit() and len(conversions[-1]) != 0:
            conversions.append([])
        elif g[0].isdigit():
            conversions[-1].append(int(g))

    locations = []
    for seed in conversions[0]:
        value = seed
        for con in conversions[1:]:
            for i in range(0, len(con), 3):
                triplet = con[i: i+3]
                if triplet[1] + triplet[2] > value >= triplet[1]:
                    diff = value - triplet[1]
                    value = triplet[0] + diff
                    break
        locations.append(value)
    return min(locations)

def day5_extra():
    with open('inputs/day5.txt', 'r') as f:
        grid = f.read()

    grid = [token for token in re.split(r'[:\n\s]', grid) if token != '']
    conversions = [[]]
    for g in grid:
        if not g[0].isdigit() and len(conversions[-1]) != 0:
            conversions.append([])
        elif g[0].isdigit():
            conversions[-1].append(int(g))

    locations = []
    # must make it better with ranges
    return min(locations)
