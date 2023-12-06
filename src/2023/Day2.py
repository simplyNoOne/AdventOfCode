import re


def day2_base():
    f = open('inputs/day2.txt', 'r')

    color_max = {'red': 12, 'green': 13, 'blue': 14}

    result = 0
    game = 0
    while True:
        line = f.readline()
        if not line:
            break
        game += 1
        tokens = re.split(r'[,;:\s]', line)
        tokens = [tok for tok in tokens if tok != ''][2:]
        correct = True
        for i in range(1, len(tokens), 2):
            if color_max[tokens[i]] < int(tokens[i - 1]):
                correct = False
                break
        if correct:
            result += game
    f.close()
    return result


def day2_extra():
    f = open('inputs/day2.txt', 'r')

    result = 0
    game = 0
    while True:
        color_max = {'red': 0, 'green': 0, 'blue': 0}
        line = f.readline()
        if not line:
            break
        game += 1
        tokens = re.split(r'[,;:\s]', line)
        tokens = [tok for tok in tokens if tok != ''][2:]
        for i in range(1, len(tokens), 2):
            if color_max[tokens[i]] < int(tokens[i - 1]):
                color_max[tokens[i]] = int(tokens[i - 1])
        result += (color_max['red'] * color_max['green'] * color_max['blue'])
    f.close()
    return result

