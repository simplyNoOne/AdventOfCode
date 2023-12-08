import re
import math


def day8_base():
    with open('inputs/day8.txt') as f:
        directions = f.readline().split("\n")[0]
        f.readline()
        list_dir = []
        while line := f.readline():
            list_dir.append([ex for ex in re.split(r'[=,\n()\s]', line) if ex != ""])

    pos = 'AAA'
    dest = 'ZZZ'

    map_dict = {}
    for entry in list_dir:
        map_dict[entry[0]] = [entry[1], entry[2]]

    return count_steps(pos, dest, directions, map_dict)


def count_steps(pos, dest, directions, map_dict):
    direction_id = 0
    steps = 0
    while pos != dest:
        if direction_id == len(directions):
            direction_id = 0
        if directions[direction_id] == 'L':
            pos = map_dict[pos][0]
        else:
            pos = map_dict[pos][1]
        direction_id += 1
        steps += 1

    return steps


def day8_extra():
    with open('inputs/day8.txt') as f:
        directions = f.readline().split("\n")[0]
        f.readline()
        list_dir = []
        while line := f.readline():
            list_dir.append([ex for ex in re.split(r'[=,\n()\s]', line) if ex != ""])

    map_dict = {}
    locs = []

    for entry in list_dir:
        map_dict[entry[0]] = [entry[1], entry[2]]
        if entry[0][2] == 'A':
            locs.append(entry[0])

    steps = []
    for loc in locs:
        steps.append(count_steps_multi(loc, directions, map_dict))

    number = steps[0]
    for i in range(1, len(steps)):
        number = lcm(number, steps[i])
    return number


def count_steps_multi(pos, directions, map_dict):
    direction_id = 0
    steps = 0
    while pos[2] != 'Z':
        if direction_id == len(directions):
            direction_id = 0
        if directions[direction_id] == 'L':
            pos = map_dict[pos][0]
        else:
            pos = map_dict[pos][1]
        direction_id += 1
        steps += 1
    return steps


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
