import re


def check_cycle(cycle, X):
    if (cycle+20) % 40 == 0:
        return cycle*X
    return 0


def day10_base():
    f = open('inputs/day10.txt', 'r')
    cycle = 1
    x = 1
    signal_sum = 0
    while True:
        cycle_add = 0
        op = f.readline()
        if not op:
            break
        inst = re.split(' |\n', op)
        if inst[0] == 'addx':
            signal_sum += check_cycle(cycle, x)
            cycle += 1
            cycle_add = int(inst[1])
        signal_sum += check_cycle(cycle, x)
        cycle += 1
        x += cycle_add
    f.close()
    print('Sum of the signals: ' + str(signal_sum))


def draw(image, cycle, x):
    if cycle != 1 and cycle % 40 == 1:
        image += '\n'
        x += 40
    if abs(x - (cycle-1)) <= 1:
        image += '#'
    else:
        image += '.'
    cycle += 1
    return image, cycle, x


def day10_extra():
    f = open('inputs/day10.txt', 'r')
    image = ''
    cycle = 1
    x = 1
    while True:
        op = f.readline()
        if not op:
            break
        inst = re.split(' |\n', op)
        cycle_add = 0
        if inst[0] == 'addx':
            image, cycle, x = draw(image=image, cycle=cycle, x=x)
            cycle_add = int(inst[1])
        image, cycle, x = draw(image=image, cycle=cycle, x=x)
        x += cycle_add
    f.close()
    print("Image:")
    print(image)

