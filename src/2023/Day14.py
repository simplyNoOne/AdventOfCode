def day14_base():
    dish = []
    with open('inputs/day14.txt') as f:
        while line := f.readline():
            dish.append(line.split("\n")[0])

    print(dish)
    dish_w = len(dish[0])
    dish_h = len(dish)

    offsets = [0] * dish_w
    rocks = []
    for _ in range(dish_w):
        rocks.append([])

    for i, row in enumerate(dish):
        for j, spot in enumerate(row):
            if spot == 'O':
                if len(rocks[j]) > 0 and rocks[j][-1] + 1 > offsets[j]:
                    rocks[j].append(rocks[j][-1] + 1)
                else:
                    rocks[j].append(offsets[j])
            elif spot == '#':
                offsets[j] = i + 1
    total_load = 0
    for i, row in enumerate(rocks):
        for j, depth in enumerate(row):
            total_load += (dish_h - depth)

    return total_load
